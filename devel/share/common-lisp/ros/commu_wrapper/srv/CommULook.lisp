; Auto-generated. Do not edit!


(cl:in-package commu_wrapper-srv)


;//! \htmlinclude CommULook-request.msg.html

(cl:defclass <CommULook-request> (roslisp-msg-protocol:ros-message)
  ((look_x
    :reader look_x
    :initarg :look_x
    :type cl:integer
    :initform 0)
   (look_y
    :reader look_y
    :initarg :look_y
    :type cl:integer
    :initform 0)
   (look_z
    :reader look_z
    :initarg :look_z
    :type cl:integer
    :initform 0))
)

(cl:defclass CommULook-request (<CommULook-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CommULook-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CommULook-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name commu_wrapper-srv:<CommULook-request> is deprecated: use commu_wrapper-srv:CommULook-request instead.")))

(cl:ensure-generic-function 'look_x-val :lambda-list '(m))
(cl:defmethod look_x-val ((m <CommULook-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:look_x-val is deprecated.  Use commu_wrapper-srv:look_x instead.")
  (look_x m))

(cl:ensure-generic-function 'look_y-val :lambda-list '(m))
(cl:defmethod look_y-val ((m <CommULook-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:look_y-val is deprecated.  Use commu_wrapper-srv:look_y instead.")
  (look_y m))

(cl:ensure-generic-function 'look_z-val :lambda-list '(m))
(cl:defmethod look_z-val ((m <CommULook-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:look_z-val is deprecated.  Use commu_wrapper-srv:look_z instead.")
  (look_z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CommULook-request>) ostream)
  "Serializes a message object of type '<CommULook-request>"
  (cl:let* ((signed (cl:slot-value msg 'look_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'look_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'look_z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CommULook-request>) istream)
  "Deserializes a message object of type '<CommULook-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'look_x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'look_y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'look_z) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CommULook-request>)))
  "Returns string type for a service object of type '<CommULook-request>"
  "commu_wrapper/CommULookRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommULook-request)))
  "Returns string type for a service object of type 'CommULook-request"
  "commu_wrapper/CommULookRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CommULook-request>)))
  "Returns md5sum for a message object of type '<CommULook-request>"
  "586b9328c974a82a91e07618b791be94")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CommULook-request)))
  "Returns md5sum for a message object of type 'CommULook-request"
  "586b9328c974a82a91e07618b791be94")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CommULook-request>)))
  "Returns full string definition for message of type '<CommULook-request>"
  (cl:format cl:nil "~%~%~%~%int32 look_x~%~%~%int32 look_y~%~%~%int32 look_z~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CommULook-request)))
  "Returns full string definition for message of type 'CommULook-request"
  (cl:format cl:nil "~%~%~%~%int32 look_x~%~%~%int32 look_y~%~%~%int32 look_z~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CommULook-request>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CommULook-request>))
  "Converts a ROS message object to a list"
  (cl:list 'CommULook-request
    (cl:cons ':look_x (look_x msg))
    (cl:cons ':look_y (look_y msg))
    (cl:cons ':look_z (look_z msg))
))
;//! \htmlinclude CommULook-response.msg.html

(cl:defclass <CommULook-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass CommULook-response (<CommULook-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CommULook-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CommULook-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name commu_wrapper-srv:<CommULook-response> is deprecated: use commu_wrapper-srv:CommULook-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <CommULook-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:success-val is deprecated.  Use commu_wrapper-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CommULook-response>) ostream)
  "Serializes a message object of type '<CommULook-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CommULook-response>) istream)
  "Deserializes a message object of type '<CommULook-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CommULook-response>)))
  "Returns string type for a service object of type '<CommULook-response>"
  "commu_wrapper/CommULookResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommULook-response)))
  "Returns string type for a service object of type 'CommULook-response"
  "commu_wrapper/CommULookResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CommULook-response>)))
  "Returns md5sum for a message object of type '<CommULook-response>"
  "586b9328c974a82a91e07618b791be94")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CommULook-response)))
  "Returns md5sum for a message object of type 'CommULook-response"
  "586b9328c974a82a91e07618b791be94")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CommULook-response>)))
  "Returns full string definition for message of type '<CommULook-response>"
  (cl:format cl:nil "~%~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CommULook-response)))
  "Returns full string definition for message of type 'CommULook-response"
  (cl:format cl:nil "~%~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CommULook-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CommULook-response>))
  "Converts a ROS message object to a list"
  (cl:list 'CommULook-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'CommULook)))
  'CommULook-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'CommULook)))
  'CommULook-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommULook)))
  "Returns string type for a service object of type '<CommULook>"
  "commu_wrapper/CommULook")