;; Auto-generated. Do not edit!


(when (boundp 'commu_helper::ClassifiedObject)
  (if (not (find-package "COMMU_HELPER"))
    (make-package "COMMU_HELPER"))
  (shadow 'ClassifiedObject (find-package "COMMU_HELPER")))
(unless (find-package "COMMU_HELPER::CLASSIFIEDOBJECT")
  (make-package "COMMU_HELPER::CLASSIFIEDOBJECT"))

(in-package "ROS")
;;//! \htmlinclude ClassifiedObject.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass commu_helper::ClassifiedObject
  :super ros::object
  :slots (_header _score _label _bbox ))

(defmethod commu_helper::ClassifiedObject
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:score __score) 0.0)
    ((:label __label) (instance std_msgs::String :init))
    ((:bbox __bbox) (instance commu_helper::BoundingBox :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _score (float __score))
   (setq _label __label)
   (setq _bbox __bbox)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:score
   (&optional __score)
   (if __score (setq _score __score)) _score)
  (:label
   (&rest __label)
   (if (keywordp (car __label))
       (send* _label __label)
     (progn
       (if __label (setq _label (car __label)))
       _label)))
  (:bbox
   (&rest __bbox)
   (if (keywordp (car __bbox))
       (send* _bbox __bbox)
     (progn
       (if __bbox (setq _bbox (car __bbox)))
       _bbox)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _score
    8
    ;; std_msgs/String _label
    (send _label :serialization-length)
    ;; commu_helper/BoundingBox _bbox
    (send _bbox :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _score
       (sys::poke _score (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; std_msgs/String _label
       (send _label :serialize s)
     ;; commu_helper/BoundingBox _bbox
       (send _bbox :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _score
     (setq _score (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; std_msgs/String _label
     (send _label :deserialize buf ptr-) (incf ptr- (send _label :serialization-length))
   ;; commu_helper/BoundingBox _bbox
     (send _bbox :deserialize buf ptr-) (incf ptr- (send _bbox :serialization-length))
   ;;
   self)
  )

(setf (get commu_helper::ClassifiedObject :md5sum-) "b202e404f3f0348d886cbf8b47d95083")
(setf (get commu_helper::ClassifiedObject :datatype-) "commu_helper/ClassifiedObject")
(setf (get commu_helper::ClassifiedObject :definition-)
      "# A message representing an object that was classified using caffe.
Header header

# The certainty of the classification from 0 to 1
float64 score

# The label attached to this object
std_msgs/String label

# The bounding box for the classified object
BoundingBox bbox
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: std_msgs/String
string data

================================================================================
MSG: commu_helper/BoundingBox
# A simple 2d bounding box message

float64 x_min
float64 y_min
float64 x_size
float64 y_size
")



(provide :commu_helper/ClassifiedObject "b202e404f3f0348d886cbf8b47d95083")


