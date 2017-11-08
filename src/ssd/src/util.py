import random
import time

import cv2
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import skimage.io

# Necessary to transform ROS images into OpenCv images for caffe
bridge = CvBridge()


def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        retval = func(*args, **kwargs)
        end_ts = time.time()
        print("elapsed time: %f" % (end_ts - beg_ts))
        return retval

    return wrapper


def draw_bounding_boxes(cv_image, classification_results):
    '''
    Draws classification bounding boxes on image
    :param image_data: The image in opencv format.
    :param classification_results: The results from classifying this image
    :return: The image, with bounding boxes and labels explaining the classification.
    '''

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    fontScale = 1
    fontThickness = 1
    text_margin = 5

    for result in classification_results:
        top_left = np.array((result.xmin, result.ymin))
        bottom_right = np.array((result.xmax, result.ymax))

        text = '{:.2f}: {}'.format(result.score, result.label_name)

        color = random_color()

        cv2.rectangle(cv_image, (top_left[0], top_left[1]), (bottom_right[0], bottom_right[1]), color, thickness=1)

        text_width, text_height = cv2.getTextSize(text, font, fontScale, fontThickness)[0]

        text_bottom_left = top_left + np.array((text_margin, -text_margin))
        text_top_right = text_bottom_left + np.array((text_width, -text_height))

        cv2.rectangle(cv_image, (text_bottom_left[0] - text_margin, text_bottom_left[1] + text_margin), (text_top_right[0] + text_margin*2, text_top_right[1] - text_margin*2), (color[0], color[1], color[2]), thickness=cv2.FILLED)

        cv2.putText(cv_image, text, (text_bottom_left[0], text_bottom_left[1]), font, fontScale, (0, 0, 0), thickness=fontThickness)
    return cv_image

def image_to_opencv(image_data):
    try:
        return bridge.imgmsg_to_cv2(image_data, "bgr8")
    except CvBridgeError as e:
        print(e)


def display_opencv_image(cv_image):
    cv2.imshow('image', cv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_opencv_image(cv_image, file_path):
    cv2.imwrite(file_path, cv_image)
    print 'Image {} saved.'.format(file_path)

def random_color():
    return random.sample(xrange(0, 255), 3)
