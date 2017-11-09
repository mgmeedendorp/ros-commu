; Auto-generated. Do not edit!


(cl:in-package commu_wrapper-srv)


;//! \htmlinclude CommUUtter-request.msg.html

(cl:defclass <CommUUtter-request> (roslisp-msg-protocol:ros-message)
  ((utterance
    :reader utterance
    :initarg :utterance
    :type cl:string
    :initform "")
   (blocking
    :reader blocking
    :initarg :blocking
    :type cl:boolean
    :initform cl:nil)
   (english
    :reader english
    :initarg :english
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass CommUUtter-request (<CommUUtter-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CommUUtter-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CommUUtter-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name commu_wrapper-srv:<CommUUtter-request> is deprecated: use commu_wrapper-srv:CommUUtter-request instead.")))

(cl:ensure-generic-function 'utterance-val :lambda-list '(m))
(cl:defmethod utterance-val ((m <CommUUtter-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:utterance-val is deprecated.  Use commu_wrapper-srv:utterance instead.")
  (utterance m))

(cl:ensure-generic-function 'blocking-val :lambda-list '(m))
(cl:defmethod blocking-val ((m <CommUUtter-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:blocking-val is deprecated.  Use commu_wrapper-srv:blocking instead.")
  (blocking m))

(cl:ensure-generic-function 'english-val :lambda-list '(m))
(cl:defmethod english-val ((m <CommUUtter-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:english-val is deprecated.  Use commu_wrapper-srv:english instead.")
  (english m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CommUUtter-request>) ostream)
  "Serializes a message object of type '<CommUUtter-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'utterance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'utterance))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'blocking) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'english) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CommUUtter-request>) istream)
  "Deserializes a message object of type '<CommUUtter-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'utterance) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'utterance) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'blocking) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'english) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CommUUtter-request>)))
  "Returns string type for a service object of type '<CommUUtter-request>"
  "commu_wrapper/CommUUtterRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommUUtter-request)))
  "Returns string type for a service object of type 'CommUUtter-request"
  "commu_wrapper/CommUUtterRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CommUUtter-request>)))
  "Returns md5sum for a message object of type '<CommUUtter-request>"
  "fc4efb8806f0415eaa9b069b92459024")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CommUUtter-request)))
  "Returns md5sum for a message object of type 'CommUUtter-request"
  "fc4efb8806f0415eaa9b069b92459024")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CommUUtter-request>)))
  "Returns full string definition for message of type '<CommUUtter-request>"
  (cl:format cl:nil "~%string utterance~%~%~%~%bool blocking~%~%~%~%bool english~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CommUUtter-request)))
  "Returns full string definition for message of type 'CommUUtter-request"
  (cl:format cl:nil "~%string utterance~%~%~%~%bool blocking~%~%~%~%bool english~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CommUUtter-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'utterance))
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CommUUtter-request>))
  "Converts a ROS message object to a list"
  (cl:list 'CommUUtter-request
    (cl:cons ':utterance (utterance msg))
    (cl:cons ':blocking (blocking msg))
    (cl:cons ':english (english msg))
))
;//! \htmlinclude CommUUtter-response.msg.html

(cl:defclass <CommUUtter-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass CommUUtter-response (<CommUUtter-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CommUUtter-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CommUUtter-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name commu_wrapper-srv:<CommUUtter-response> is deprecated: use commu_wrapper-srv:CommUUtter-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <CommUUtter-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader commu_wrapper-srv:success-val is deprecated.  Use commu_wrapper-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CommUUtter-response>) ostream)
  "Serializes a message object of type '<CommUUtter-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CommUUtter-response>) istream)
  "Deserializes a message object of type '<CommUUtter-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CommUUtter-response>)))
  "Returns string type for a service object of type '<CommUUtter-response>"
  "commu_wrapper/CommUUtterResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommUUtter-response)))
  "Returns string type for a service object of type 'CommUUtter-response"
  "commu_wrapper/CommUUtterResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CommUUtter-response>)))
  "Returns md5sum for a message object of type '<CommUUtter-response>"
  "fc4efb8806f0415eaa9b069b92459024")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CommUUtter-response)))
  "Returns md5sum for a message object of type 'CommUUtter-response"
  "fc4efb8806f0415eaa9b069b92459024")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CommUUtter-response>)))
  "Returns full string definition for message of type '<CommUUtter-response>"
  (cl:format cl:nil "~%bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CommUUtter-response)))
  "Returns full string definition for message of type 'CommUUtter-response"
  (cl:format cl:nil "~%bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CommUUtter-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CommUUtter-response>))
  "Converts a ROS message object to a list"
  (cl:list 'CommUUtter-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'CommUUtter)))
  'CommUUtter-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'CommUUtter)))
  'CommUUtter-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CommUUtter)))
  "Returns string type for a service object of type '<CommUUtter>"
  "commu_wrapper/CommUUtter")