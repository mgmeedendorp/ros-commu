#!/usr/bin/env python
import rospy

# to get commandline arguments
import sys

# Because of transformations
import std_msgs
import tf
import tf2_ros
import geometry_msgs


def broadcast_euclid_transform(tx, ty, tz, rx, ry, rz):
    pass


if __name__ == '__main__':
    tx = float(sys.argv[1])  # this is ROS coordinates, so in meters and radians
    ty = float(sys.argv[2])
    tz = float(sys.argv[3])
    rx = float(sys.argv[4])
    ry = float(sys.argv[5])
    rz = float(sys.argv[6])

    rospy.init_node("transform_broadcast_tester")
    rotation = tf.transformations.quaternion_from_euler(rx, ry, rz)

    br = tf2_ros.StaticTransformBroadcaster()

    t = geometry_msgs.msg.TransformStamped()
    t.header = std_msgs.msg.Header()
    t.header.frame_id = "camera_link"  # from `camera_link` (provided by euclid)
    t.header.stamp = rospy.Time.now(),
    t.child_frame_id = "commu_link",  # Publish a transform to `commu_link` (the origin of the commu coordinate system)
    t.transform.translation.x = tx
    t.transform.translation.y = ty
    t.transform.translation.z = tz

    t.transform.rotation.x = rotation[0]
    t.transform.rotation.y = rotation[1]
    t.transform.rotation.z = rotation[2]
    t.transform.rotation.w = rotation[3]

    rospy.loginfo(t)

    br.sendTransform(t)

    rospy.loginfo("Euclid static tranform published.")

    rospy.spin()
