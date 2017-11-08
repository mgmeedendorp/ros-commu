; Auto-generated. Do not edit!


(cl:in-package button_input-srv)


;//! \htmlinclude BinaryButtonInput-request.msg.html

(cl:defclass <BinaryButtonInput-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass BinaryButtonInput-request (<BinaryButtonInput-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BinaryButtonInput-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BinaryButtonInput-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name button_input-srv:<BinaryButtonInput-request> is deprecated: use button_input-srv:BinaryButtonInput-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BinaryButtonInput-request>) ostream)
  "Serializes a message object of type '<BinaryButtonInput-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BinaryButtonInput-request>) istream)
  "Deserializes a message object of type '<BinaryButtonInput-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BinaryButtonInput-request>)))
  "Returns string type for a service object of type '<BinaryButtonInput-request>"
  "button_input/BinaryButtonInputRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BinaryButtonInput-request)))
  "Returns string type for a service object of type 'BinaryButtonInput-request"
  "button_input/BinaryButtonInputRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BinaryButtonInput-request>)))
  "Returns md5sum for a message object of type '<BinaryButtonInput-request>"
  "59064532f110d857c53f36f4ab7ad30a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BinaryButtonInput-request)))
  "Returns md5sum for a message object of type 'BinaryButtonInput-request"
  "59064532f110d857c53f36f4ab7ad30a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BinaryButtonInput-request>)))
  "Returns full string definition for message of type '<BinaryButtonInput-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BinaryButtonInput-request)))
  "Returns full string definition for message of type 'BinaryButtonInput-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BinaryButtonInput-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BinaryButtonInput-request>))
  "Converts a ROS message object to a list"
  (cl:list 'BinaryButtonInput-request
))
;//! \htmlinclude BinaryButtonInput-response.msg.html

(cl:defclass <BinaryButtonInput-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BinaryButtonInput-response (<BinaryButtonInput-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BinaryButtonInput-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BinaryButtonInput-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name button_input-srv:<BinaryButtonInput-response> is deprecated: use button_input-srv:BinaryButtonInput-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <BinaryButtonInput-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader button_input-srv:response-val is deprecated.  Use button_input-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BinaryButtonInput-response>) ostream)
  "Serializes a message object of type '<BinaryButtonInput-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'response)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BinaryButtonInput-response>) istream)
  "Deserializes a message object of type '<BinaryButtonInput-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'response)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BinaryButtonInput-response>)))
  "Returns string type for a service object of type '<BinaryButtonInput-response>"
  "button_input/BinaryButtonInputResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BinaryButtonInput-response)))
  "Returns string type for a service object of type 'BinaryButtonInput-response"
  "button_input/BinaryButtonInputResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BinaryButtonInput-response>)))
  "Returns md5sum for a message object of type '<BinaryButtonInput-response>"
  "59064532f110d857c53f36f4ab7ad30a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BinaryButtonInput-response)))
  "Returns md5sum for a message object of type 'BinaryButtonInput-response"
  "59064532f110d857c53f36f4ab7ad30a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BinaryButtonInput-response>)))
  "Returns full string definition for message of type '<BinaryButtonInput-response>"
  (cl:format cl:nil "uint8 response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BinaryButtonInput-response)))
  "Returns full string definition for message of type 'BinaryButtonInput-response"
  (cl:format cl:nil "uint8 response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BinaryButtonInput-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BinaryButtonInput-response>))
  "Converts a ROS message object to a list"
  (cl:list 'BinaryButtonInput-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'BinaryButtonInput)))
  'BinaryButtonInput-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'BinaryButtonInput)))
  'BinaryButtonInput-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BinaryButtonInput)))
  "Returns string type for a service object of type '<BinaryButtonInput>"
  "button_input/BinaryButtonInput")