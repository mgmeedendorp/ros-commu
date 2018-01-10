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


    if len(sys.argv) < 8:
        rospy.logerr(
            'Invalid number of parameters\nusage: ./static_turtle_tf2_broadcaster.py child_frame_name x y z roll pitch yaw')
        sys.exit(0)
    else:
        if sys.argv[1] == 'world':
            rospy.logerr('Your static turtle name cannot be "world"')
            sys.exit(0)

        rospy.init_node('my_static_tf2_broadcaster')
        broadcaster = tf2_ros.StaticTransformBroadcaster()
        static_transformStamped = geometry_msgs.msg.TransformStamped()

        static_transformStamped.header.stamp = rospy.Time.now()
        static_transformStamped.header.frame_id = "world"
        static_transformStamped.child_frame_id = sys.argv[1]

        static_transformStamped.transform.translation.x = float(sys.argv[2])
        static_transformStamped.transform.translation.y = float(sys.argv[3])
        static_transformStamped.transform.translation.z = float(sys.argv[4])

        quat = tf.transformations.quaternion_from_euler(float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]))
        static_transformStamped.transform.rotation.x = quat[0]
        static_transformStamped.transform.rotation.y = quat[1]
        static_transformStamped.transform.rotation.z = quat[2]
        static_transformStamped.transform.rotation.w = quat[3]

        broadcaster.sendTransform(static_transformStamped)
        rospy.spin()