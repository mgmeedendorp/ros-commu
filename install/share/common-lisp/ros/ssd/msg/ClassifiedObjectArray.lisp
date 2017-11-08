; Auto-generated. Do not edit!


(cl:in-package ssd-msg)


;//! \htmlinclude ClassifiedObjectArray.msg.html

(cl:defclass <ClassifiedObjectArray> (roslisp-msg-protocol:ros-message)
  ((objects
    :reader objects
    :initarg :objects
    :type (cl:vector ssd-msg:ClassifiedObject)
   :initform (cl:make-array 0 :element-type 'ssd-msg:ClassifiedObject :initial-element (cl:make-instance 'ssd-msg:ClassifiedObject))))
)

(cl:defclass ClassifiedObjectArray (<ClassifiedObjectArray>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ClassifiedObjectArray>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ClassifiedObjectArray)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ssd-msg:<ClassifiedObjectArray> is deprecated: use ssd-msg:ClassifiedObjectArray instead.")))

(cl:ensure-generic-function 'objects-val :lambda-list '(m))
(cl:defmethod objects-val ((m <ClassifiedObjectArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ssd-msg:objects-val is deprecated.  Use ssd-msg:objects instead.")
  (objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ClassifiedObjectArray>) ostream)
  "Serializes a message object of type '<ClassifiedObjectArray>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ClassifiedObjectArray>) istream)
  "Deserializes a message object of type '<ClassifiedObjectArray>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'objects) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'objects)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ssd-msg:ClassifiedObject))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ClassifiedObjectArray>)))
  "Returns string type for a message object of type '<ClassifiedObjectArray>"
  "ssd/ClassifiedObjectArray")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ClassifiedObjectArray)))
  "Returns string type for a message object of type 'ClassifiedObjectArray"
  "ssd/ClassifiedObjectArray")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ClassifiedObjectArray>)))
  "Returns md5sum for a message object of type '<ClassifiedObjectArray>"
  "59f286ee6aa871e16584f755f2af5a21")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ClassifiedObjectArray)))
  "Returns md5sum for a message object of type 'ClassifiedObjectArray"
  "59f286ee6aa871e16584f755f2af5a21")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ClassifiedObjectArray>)))
  "Returns full string definition for message of type '<ClassifiedObjectArray>"
  (cl:format cl:nil "# An array of ClassifiedObject messages~%~%ClassifiedObject[] objects~%================================================================================~%MSG: ssd/ClassifiedObject~%# A message representing an object that was classified using caffe.~%Header header~%~%# The certainty of the classification from 0 to 1~%float64 score~%~%# The label attached to this object~%string label~%~%# The bounding box for the classified object~%BoundingBox bbox~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ssd/BoundingBox~%# A simple 2d bounding box message~%~%float64 x_min~%float64 y_min~%float64 x_size~%float64 y_size~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ClassifiedObjectArray)))
  "Returns full string definition for message of type 'ClassifiedObjectArray"
  (cl:format cl:nil "# An array of ClassifiedObject messages~%~%ClassifiedObject[] objects~%================================================================================~%MSG: ssd/ClassifiedObject~%# A message representing an object that was classified using caffe.~%Header header~%~%# The certainty of the classification from 0 to 1~%float64 score~%~%# The label attached to this object~%string label~%~%# The bounding box for the classified object~%BoundingBox bbox~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ssd/BoundingBox~%# A simple 2d bounding box message~%~%float64 x_min~%float64 y_min~%float64 x_size~%float64 y_size~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ClassifiedObjectArray>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ClassifiedObjectArray>))
  "Converts a ROS message object to a list"
  (cl:list 'ClassifiedObjectArray
    (cl:cons ':objects (objects msg))
))
