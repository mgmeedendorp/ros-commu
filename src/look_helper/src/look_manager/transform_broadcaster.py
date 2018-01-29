#!/usr/bin/env python
import math
# to get commandline arguments
import sys

import geometry_msgs
import rospy
# Because of transformations
import std_msgs
import tf
import tf2_ros
from geometry_msgs.msg import TransformStamped
from image_geometry import PinholeCameraModel
from realsense_person.msg import PersonDetection
from rospy import Time
from sensor_msgs.msg import CameraInfo
from ssd.msg import ClassifiedObject


def publish_person_transform(tx, ty, tz):
    publish_dynamic_transform_euclidean(
        "camera_depth_optical_frame",
        "person",
        tx, ty, tz,
        0, 0, 0
    )


def publish_euclid_transform(tx, ty, tz, rx, ry, rz):
    publish_static_transform_euclidean(
        "commu_link",
        "camera_link",
        tx, ty, tz,
        rx, ry, rz
    )

def publish_webcam_transform(tx, ty, tz, rx, ry, rz):
    publish_static_transform_euclidean(
        "commu_link",
        "webcam_frame",
        tx, ty, tz,
        rx, ry, rz
    )

    publish_static_transform_euclidean(
        "webcam_frame",
        "webcam_frame_optical",
        0, 0, 0,
        math.radians(-90), 0, math.radians(-90)
    )


def publish_object_transform(camera_info, objects, distance_from_camera=0.5):
    # type: (CameraInfo, list[ClassifiedObject], float, float, float) -> None
    """
    This function publishes the 3d transform of a list of ClassifiedObjects by projecting them on a plane that is
    `distance_from_camera` meters in front of the camera.
    :param camera_info: The CameraInfo object for the camera used to classify objects.
    :param objects: The list of ClassifiedObjects for which to publish a transform.
    :param distance_from_camera: The distance of the plane to project the objects on from the camera.
    """

    camera = PinholeCameraModel()
    camera.fromCameraInfo(camera_info)

    for object in objects:
        obj_center_x = (object.bbox.x_min + object.bbox.x_size / 2.0)
        obj_center_y = (object.bbox.y_min + object.bbox.y_size / 2.0)

        obj_center_rectified = camera.rectifyPoint((obj_center_x, obj_center_y))

        ray = camera.projectPixelTo3dRay(obj_center_rectified)

        coordinate = (
            ray[0] * distance_from_camera,
            ray[1] * distance_from_camera,
            ray[2] * distance_from_camera
        )

        publish_dynamic_transform_euclidean(
            "webcam_frame_optical",
            object.id,
            coordinate[0], coordinate[1], coordinate[2],
            0, 0, 0
        )


def publish_commu_head_yaw_transform():
    publish_static_transform_euclidean(
        "commu_link",
        "commu_head_yaw",
        0, 0, .2,
        0, 0, 0
    )


def publish_static_transform_euclidean(parent, child, tx, ty, tz, rx, ry, rz):
    # type: (str, str, float, float, float, float, float, float) -> None
    """
    Publishes a static transform at the current time from the parent frame to the child frame.
    :param parent: The name of the parent frame of reference for this transform
    :param child: The name of the child frame of reference for this transform
    :param tx: The translation from the parent to the child frame on the x axis of the ROS coordinate system in meters.
    :param ty: The translation from the parent to the child frame on the y axis of the ROS coordinate system in meters.
    :param tz: The translation from the parent to the child frame on the z axis of the ROS coordinate system in meters.
    :param rx: The euclidean rotation around from the parent to the child frame on the the x-axis of the ROS coordinate system in radians.
    :param ry: The euclidean rotation around from the parent to the child frame on the the y-axis of the ROS coordinate system in radians.
    :param rz: The euclidean rotation around from the parent to the child frame on the the z-axis of the ROS coordinate system in radians.
    """

    qx, qy, qz, qw = tf.transformations.quaternion_from_euler(rx, ry, rz)

    publish_static_transform_quaternion(
        rospy.Time.now(),
        parent,
        child,
        tx, ty, tz,
        qx, qy, qz, qw
    )


def publish_static_transform_quaternion(time, parent, child, tx, ty, tz, rx, ry, rz, rw):
    # type: (Time, str, str, float, float, float, float, float, float, float) -> None
    """
    Publishes a static transform at the specified time from the parent frame to the child frame.
    :param time: The time to pass to the message header.
    :param parent: The name of the parent frame of reference for this transform
    :param child: The name of the child frame of reference for this transform
    :param tx: The translation from the parent to the child frame on the x axis of the ROS coordinate system in meters.
    :param ty: The translation from the parent to the child frame on the y axis of the ROS coordinate system in meters.
    :param tz: The translation from the parent to the child frame on the z axis of the ROS coordinate system in meters.
    :param rx: The x-component rotation from the parent to the child frame in quaternion form of the ROS coordinate system.
    :param ry: The y-component rotation from the parent to the child frame in quaternion form of the ROS coordinate system.
    :param rz: The z-component rotation from the parent to the child frame in quaternion form of the ROS coordinate system.
    :param rw: The w-component rotation from the parent to the child frame in quaternion form of the ROS coordinate system.
    """

    br = tf2_ros.StaticTransformBroadcaster()

    t = geometry_msgs.msg.TransformStamped()
    t.header = std_msgs.msg.Header()
    t.header.frame_id = parent
    t.header.stamp = time
    t.child_frame_id = child
    t.transform.translation.x = tx
    t.transform.translation.y = ty
    t.transform.translation.z = tz

    t.transform.rotation.x = rx
    t.transform.rotation.y = ry
    t.transform.rotation.z = rz
    t.transform.rotation.w = rw

    br.sendTransform(t)

    rospy.loginfo("Static transform from '" + parent + "' to '" + child + "' published.")


def publish_dynamic_transform_euclidean(parent, child, tx, ty, tz, rx, ry, rz):
    br = tf.TransformBroadcaster()

    rotation = tf.transformations.quaternion_from_euler(rx, ry, rz)

    br.sendTransform(
        (tx, ty, tz),
        rotation,
        rospy.Time.now(),
        child,
        parent
    )

    rospy.loginfo("Dynamic transform from '" + parent + "' to '" + child + "' published.")


if __name__ == '__main__':
    tx = float(sys.argv[1])  # this is ROS coordinates, so in meters and radians
    ty = float(sys.argv[2])
    tz = float(sys.argv[3])
    rx = float(sys.argv[4])
    ry = float(sys.argv[5])
    rz = float(sys.argv[6])

    rospy.init_node("transform_broadcast_tester")

    def person_callback(data):
        if len(data.persons) > 0:
            person = data.persons[0]

            center_of_mass_world = person.center_of_mass.world

            x = center_of_mass_world.x
            y = center_of_mass_world.y
            z = center_of_mass_world.z

            publish_person_transform(x, y, z)

    rospy.Subscriber("/camera/person/detection_data", PersonDetection, person_callback)

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        publish_euclid_transform(
            tx, ty, tz,
            rx, ry, rz
        )

        publish_commu_head_yaw_transform()

        try:
            transform = tfBuffer.lookup_transform("commu_head_yaw", "person", rospy.Time(), rospy.Duration(1))  # type: TransformStamped

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        rospy.loginfo("person transform yay")
        rospy.loginfo(transform)




