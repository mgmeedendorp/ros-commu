import rospy

def get_srv_function(service_name, service_cls):
    # type: (str, any) -> any
    rospy.wait_for_service(service_name)

    try:
        return rospy.ServiceProxy(service_name, service_cls)
    except rospy.ServiceException, e:
        print("Service call failed: %s" % e)
