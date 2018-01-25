; Auto-generated. Do not edit!


(cl:in-package ssd-msg)


;//! \htmlinclude ClassifiedObject.msg.html

(cl:defclass <ClassifiedObject> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (score
    :reader score
    :initarg :score
    :type cl:float
    :initform 0.0)
   (label
    :reader label
    :initarg :label
    :type cl:string
    :initform "")
   (id
    :reader id
    :initarg :id
    :type cl:string
    :initform "")
   (bbox
    :reader bbox
    :initarg :bbox
    :type ssd-msg:BoundingBox
    :initform (cl:make-instance 'ssd-msg:BoundingBox)))
)

(cl:defclass ClassifiedObject (<ClassifiedObject>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ClassifiedObject>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ClassifiedObject)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ssd-msg:<ClassifiedObject> is deprecated: use ssd-msg:ClassifiedObject instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ClassifiedObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ssd-msg:header-val is deprecated.  Use ssd-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'score-val :lambda-list '(m))
(cl:defmethod score-val ((m <ClassifiedObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ssd-msg:score-val is deprecated.  Use ssd-msg:score instead.")
  (score m))

(cl:ensure-generic-function 'label-val :lambda-list '(m))
(cl:defmethod label-val ((m <ClassifiedObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ssd-msg:label-val is deprecated.  Use ssd-msg:label instead.")
  (label m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <ClassifiedObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ssd-msg:id-val is deprecated.  Use ssd-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'bbox-val :lambda-list '(m))
(cl:defmethod bbox-val ((m <ClassifiedObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ssd-msg:bbox-val is deprecated.  Use ssd-msg:bbox instead.")
  (bbox m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ClassifiedObject>) ostream)
  "Serializes a message object of type '<ClassifiedObject>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'score))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'label))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'label))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'id))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'bbox) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ClassifiedObject>) istream)
  "Deserializes a message object of type '<ClassifiedObject>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'score) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'label) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'label) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'bbox) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ClassifiedObject>)))
  "Returns string type for a message object of type '<ClassifiedObject>"
  "ssd/ClassifiedObject")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ClassifiedObject)))
  "Returns string type for a message object of type 'ClassifiedObject"
  "ssd/ClassifiedObject")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ClassifiedObject>)))
  "Returns md5sum for a message object of type '<ClassifiedObject>"
  "fb5442e2046a6d60a459f1e47ecae020")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ClassifiedObject)))
  "Returns md5sum for a message object of type 'ClassifiedObject"
  "fb5442e2046a6d60a459f1e47ecae020")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ClassifiedObject>)))
  "Returns full string definition for message of type '<ClassifiedObject>"
  (cl:format cl:nil "# A message representing an object that was classified using caffe.~%Header header~%~%# The certainty of the classification from 0 to 1~%float64 score~%~%# The label attached to this object~%string label~%~%# The id of this object. This is only unique for one classification forom one image.~%string id~%~%# The bounding box for the classified object~%BoundingBox bbox~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ssd/BoundingBox~%# A simple 2d bounding box message~%~%float64 x_min~%float64 y_min~%float64 x_size~%float64 y_size~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ClassifiedObject)))
  "Returns full string definition for message of type 'ClassifiedObject"
  (cl:format cl:nil "# A message representing an object that was classified using caffe.~%Header header~%~%# The certainty of the classification from 0 to 1~%float64 score~%~%# The label attached to this object~%string label~%~%# The id of this object. This is only unique for one classification forom one image.~%string id~%~%# The bounding box for the classified object~%BoundingBox bbox~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ssd/BoundingBox~%# A simple 2d bounding box message~%~%float64 x_min~%float64 y_min~%float64 x_size~%float64 y_size~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ClassifiedObject>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     8
     4 (cl:length (cl:slot-value msg 'label))
     4 (cl:length (cl:slot-value msg 'id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'bbox))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ClassifiedObject>))
  "Converts a ROS message object to a list"
  (cl:list 'ClassifiedObject
    (cl:cons ':header (header msg))
    (cl:cons ':score (score msg))
    (cl:cons ':label (label msg))
    (cl:cons ':id (id msg))
    (cl:cons ':bbox (bbox msg))
))
