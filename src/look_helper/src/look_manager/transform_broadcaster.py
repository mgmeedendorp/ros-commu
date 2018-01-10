#!/usr/bin/env python
import rospy

# to get commandline arguments
import sys

# Because of transformations
import std_msgs
import tf
import tf2_ros
import geometry_msgs
from rospy import Time


def broadcast_euclid_transform(tx, ty, tz, rx, ry, rz):
    pass


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

    pass


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

if __name__ == '__main__':
    tx = float(sys.argv[1])  # this is ROS coordinates, so in meters and radians
    ty = float(sys.argv[2])
    tz = float(sys.argv[3])
    rx = float(sys.argv[4])
    ry = float(sys.argv[5])
    rz = float(sys.argv[6])

    rospy.init_node("transform_broadcast_tester")

    while not rospy.is_shutdown():
        publish_static_transform_euclidean(
            "base_link",
            "commu_link",
            tx, ty, tz,
            rx, ry, rz
        )

        publish_static_transform_euclidean(
            "commu_link",
            "commu_head_yaw",
            0, 0, .2,
            0, 0, 0
        )
