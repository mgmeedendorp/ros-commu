#!/usr/bin/env python
import rospy

# to get commandline arguments
import sys

# Because of transformations
import tf

import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
    tx = float(sys.argv[1])
    ty = float(sys.argv[2])
    tz = float(sys.argv[3])
    rx = float(sys.argv[4])
    ry = float(sys.argv[5])
    rz = float(sys.argv[6])

    rospy.init_node("transform_broadcast_tester")

    br = tf.TransformBroadcaster()
    br.sendTransform(
        (tx, ty, tz),
        tf.transformations.quaternion_from_euler(rx, ry, rz),
        rospy.Time.now(),
        "camera_link",  # Publish a transform from `camera_link` (provided by euclid)
        "commu_link"    # to `commu_link` (the origin of the commu coordinate system)
    )