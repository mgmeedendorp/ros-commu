; Auto-generated. Do not edit!


(cl:in-package ssd-msg)


;//! \htmlinclude ClassifiedObjectArray.msg.html

(cl:defclass <ClassifiedObjectArray> (roslisp-msg-protocol:ros-message)
  ((objects
    :reader objects
    :initarg :objects
    :type (cl:vector ssd-msg:ClassifiedObject)
   :initform (cl:make-array 0 :element-type 'ssd-msg:ClassifiedObject :initial-element (cl:make-instance 'ssd-msg:ClassifiedObject)))
   (image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
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

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <ClassifiedObjectArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ssd-msg:image-val is deprecated.  Use ssd-msg:image instead.")
  (image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ClassifiedObjectArray>) ostream)
  "Serializes a message object of type '<ClassifiedObjectArray>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'objects))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
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
  "ccc40aeeae1ee53272e491b81bf276de")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ClassifiedObjectArray)))
  "Returns md5sum for a message object of type 'ClassifiedObjectArray"
  "ccc40aeeae1ee53272e491b81bf276de")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ClassifiedObjectArray>)))
  "Returns full string definition for message of type '<ClassifiedObjectArray>"
  (cl:format cl:nil "# An array of ClassifiedObject messages~%~%ClassifiedObject[] objects~%~%#The classified image~%sensor_msgs/Image image~%================================================================================~%MSG: ssd/ClassifiedObject~%# A message representing an object that was classified using caffe.~%Header header~%~%# The certainty of the classification from 0 to 1~%float64 score~%~%# The label attached to this object~%string label~%~%# The bounding box for the classified object~%BoundingBox bbox~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ssd/BoundingBox~%# A simple 2d bounding box message~%~%float64 x_min~%float64 y_min~%float64 x_size~%float64 y_size~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ClassifiedObjectArray)))
  "Returns full string definition for message of type 'ClassifiedObjectArray"
  (cl:format cl:nil "# An array of ClassifiedObject messages~%~%ClassifiedObject[] objects~%~%#The classified image~%sensor_msgs/Image image~%================================================================================~%MSG: ssd/ClassifiedObject~%# A message representing an object that was classified using caffe.~%Header header~%~%# The certainty of the classification from 0 to 1~%float64 score~%~%# The label attached to this object~%string label~%~%# The bounding box for the classified object~%BoundingBox bbox~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ssd/BoundingBox~%# A simple 2d bounding box message~%~%float64 x_min~%float64 y_min~%float64 x_size~%float64 y_size~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ClassifiedObjectArray>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ClassifiedObjectArray>))
  "Converts a ROS message object to a list"
  (cl:list 'ClassifiedObjectArray
    (cl:cons ':objects (objects msg))
    (cl:cons ':image (image msg))
))
