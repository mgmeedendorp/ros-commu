; Auto-generated. Do not edit!


(cl:in-package look_helper-srv)


;//! \htmlinclude SetLookAtTarget-request.msg.html

(cl:defclass <SetLookAtTarget-request> (roslisp-msg-protocol:ros-message)
  ((target_frame_name
    :reader target_frame_name
    :initarg :target_frame_name
    :type cl:string
    :initform ""))
)

(cl:defclass SetLookAtTarget-request (<SetLookAtTarget-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetLookAtTarget-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetLookAtTarget-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name look_helper-srv:<SetLookAtTarget-request> is deprecated: use look_helper-srv:SetLookAtTarget-request instead.")))

(cl:ensure-generic-function 'target_frame_name-val :lambda-list '(m))
(cl:defmethod target_frame_name-val ((m <SetLookAtTarget-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader look_helper-srv:target_frame_name-val is deprecated.  Use look_helper-srv:target_frame_name instead.")
  (target_frame_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetLookAtTarget-request>) ostream)
  "Serializes a message object of type '<SetLookAtTarget-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'target_frame_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'target_frame_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetLookAtTarget-request>) istream)
  "Deserializes a message object of type '<SetLookAtTarget-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'target_frame_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'target_frame_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetLookAtTarget-request>)))
  "Returns string type for a service object of type '<SetLookAtTarget-request>"
  "look_helper/SetLookAtTargetRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetLookAtTarget-request)))
  "Returns string type for a service object of type 'SetLookAtTarget-request"
  "look_helper/SetLookAtTargetRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetLookAtTarget-request>)))
  "Returns md5sum for a message object of type '<SetLookAtTarget-request>"
  "1030478efebc9e6deae2c1ba1ffff144")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetLookAtTarget-request)))
  "Returns md5sum for a message object of type 'SetLookAtTarget-request"
  "1030478efebc9e6deae2c1ba1ffff144")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetLookAtTarget-request>)))
  "Returns full string definition for message of type '<SetLookAtTarget-request>"
  (cl:format cl:nil "~%~%~%string target_frame_name~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetLookAtTarget-request)))
  "Returns full string definition for message of type 'SetLookAtTarget-request"
  (cl:format cl:nil "~%~%~%string target_frame_name~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetLookAtTarget-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'target_frame_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetLookAtTarget-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetLookAtTarget-request
    (cl:cons ':target_frame_name (target_frame_name msg))
))
;//! \htmlinclude SetLookAtTarget-response.msg.html

(cl:defclass <SetLookAtTarget-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetLookAtTarget-response (<SetLookAtTarget-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetLookAtTarget-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetLookAtTarget-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name look_helper-srv:<SetLookAtTarget-response> is deprecated: use look_helper-srv:SetLookAtTarget-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetLookAtTarget-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader look_helper-srv:success-val is deprecated.  Use look_helper-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetLookAtTarget-response>) ostream)
  "Serializes a message object of type '<SetLookAtTarget-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetLookAtTarget-response>) istream)
  "Deserializes a message object of type '<SetLookAtTarget-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetLookAtTarget-response>)))
  "Returns string type for a service object of type '<SetLookAtTarget-response>"
  "look_helper/SetLookAtTargetResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetLookAtTarget-response)))
  "Returns string type for a service object of type 'SetLookAtTarget-response"
  "look_helper/SetLookAtTargetResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetLookAtTarget-response>)))
  "Returns md5sum for a message object of type '<SetLookAtTarget-response>"
  "1030478efebc9e6deae2c1ba1ffff144")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetLookAtTarget-response)))
  "Returns md5sum for a message object of type 'SetLookAtTarget-response"
  "1030478efebc9e6deae2c1ba1ffff144")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetLookAtTarget-response>)))
  "Returns full string definition for message of type '<SetLookAtTarget-response>"
  (cl:format cl:nil "~%~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetLookAtTarget-response)))
  "Returns full string definition for message of type 'SetLookAtTarget-response"
  (cl:format cl:nil "~%~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetLookAtTarget-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetLookAtTarget-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetLookAtTarget-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetLookAtTarget)))
  'SetLookAtTarget-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetLookAtTarget)))
  'SetLookAtTarget-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetLookAtTarget)))
  "Returns string type for a service object of type '<SetLookAtTarget>"
  "look_helper/SetLookAtTarget")