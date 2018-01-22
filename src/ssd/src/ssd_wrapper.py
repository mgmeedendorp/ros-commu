#!/usr/bin/env python
import os
import sys

import numpy as np
from google.protobuf import text_format
from ssd.msg import ClassifiedObjectArray, ClassifiedObject, BoundingBox

import caffe
from caffe.proto import caffe_pb2
from util import time_usage
from std_msgs.msg import Header
import rospy


class SSD:
    caffe_root = '/home/maurice/catkin_ws/src/ssd/caffe/'
    input_resolution = []

    labelmap = None

    net = None
    transformer = None

    def __init__(self, use_gpu=True):
        os.chdir(self.caffe_root)
        sys.path.insert(0, 'python')

        if (use_gpu):
            caffe.set_mode_gpu()
            caffe.set_device(0)  # TODO: No multiple GPU cores?
        else:
            caffe.set_mode_cpu()

        self.load_label_map()
        self.create_network()
        self.create_transformer()

    def load_label_map(self):
        # load PASCAL VOC labels
        labelmap_file = self.caffe_root + 'data/VOC0712/labelmap_voc.prototxt'
        file = open(labelmap_file, 'r')
        labelmap = caffe_pb2.LabelMap()
        text_format.Merge(str(file.read()), labelmap)
        self.labelmap = labelmap

    def create_network(self):
        model_def = self.caffe_root + 'models/VGGNet/VOC0712/SSD_300x300/deploy.prototxt'
        model_weights = self.caffe_root + 'models/VGGNet/VOC0712/SSD_300x300/VGG_VOC0712_SSD_300x300_iter_120000.caffemodel'

        self.net = caffe.Net(model_def,  # defines the structure of the model
                             model_weights,  # contains the trained weights
                             caffe.TEST)  # use test mode (e.g., don't perform dropout)

    def create_transformer(self):
        # input preprocessing: 'data' is the name of the input blob == net.inputs[0]
        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_transpose('data', (2, 0, 1))
        self.transformer.set_mean('data', np.array([104, 117, 123]))  # mean pixel
        #self.transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
        #self.transformer.set_channel_swap('data', (2, 1, 0))  # the reference model has channels in BGR order instead of RGB

    def get_label_name(self, labels):
        if self.labelmap is None:
            self.load_label_map()

        num_labels = len(self.labelmap.item)
        labelnames = []
        if type(labels) is not list:
            labels = [labels]
        for label in labels:
            found = False
            for i in xrange(0, num_labels):
                if label == self.labelmap.item[i].label:
                    found = True
                    labelnames.append(self.labelmap.item[i].display_name)
                    break
            assert found == True
        return labelnames

    @time_usage
    def classify_image(self, cv_image, min_confidence=0.6):
        transformed_image = self.transformer.preprocess('data', cv_image)
        self.net.blobs['data'].data[...] = transformed_image

        # Runs a forward pass with the image
        detections = self.net.forward()['detection_out']

        # Parse the outputs.
        det_label = detections[0, 0, :, 1]
        det_conf = detections[0, 0, :, 2]
        det_xmin = detections[0, 0, :, 3]
        det_ymin = detections[0, 0, :, 4]
        det_xmax = detections[0, 0, :, 5]
        det_ymax = detections[0, 0, :, 6]

        # Get detections with confidence higher than 0.6.
        top_indices = [i for i, conf in enumerate(det_conf) if conf >= min_confidence]

        top_conf = det_conf[top_indices]
        top_label_indices = det_label[top_indices].tolist()
        top_labels = self.get_label_name(top_label_indices)
        top_xmin = det_xmin[top_indices]
        top_ymin = det_ymin[top_indices]
        top_xmax = det_xmax[top_indices]
        top_ymax = det_ymax[top_indices]

        for i in range(0, len(top_indices)):
            rospy.loginfo('detection {}: <{:.2}: {}>'.format(i, top_conf[i], top_labels[i]))

        results = []

        for i in xrange(top_conf.shape[0]):
            height, width = cv_image.shape[:2]

            xmin = int(round(top_xmin[i] * width))
            ymin = int(round(top_ymin[i] * height))
            xmax = int(round(top_xmax[i] * width))
            ymax = int(round(top_ymax[i] * height))
            score = top_conf[i]
            label_name = top_labels[i]

            results.append(ClassificationResult(score, label_name, xmin, ymin, xmax, ymax))

        return results


class ClassificationResult:
    def __init__(self, score, label_name, xmin, ymin, xmax, ymax):
        self.score = score
        self.label_name = label_name
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def get_center(self):
        return [self.xmin + (self.get_width() / 2), self.ymin + (self.get_height() / 2)]

    def get_width(self):
        return self.xmax - self.xmin

    def get_height(self):
        return self.ymax - self.ymin

    def to_msg(self):
        msg = ClassifiedObject()

        msg.header = Header()
        msg.header.stamp = rospy.Time.now()

        msg.bbox = BoundingBox()
        msg.bbox.x_min = self.xmin
        msg.bbox.y_min = self.ymin
        msg.bbox.x_size = self.get_width()
        msg.bbox.y_size = self.get_height()

        msg.label = self.label_name
        msg.score = self.score

        return msg

    def to_string(self):
        return '{} detected with a confidence of {} at ({}, {}), with size ({}, {})'.format(
            self.label_name,
            self.score,
            self.xmin,
            self.ymin,
            self.xmax - self.xmin + 1,
            self.ymax - self.ymin + 1
        )
