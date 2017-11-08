;; Auto-generated. Do not edit!


(when (boundp 'ssd::ClassifiedObject)
  (if (not (find-package "SSD"))
    (make-package "SSD"))
  (shadow 'ClassifiedObject (find-package "SSD")))
(unless (find-package "SSD::CLASSIFIEDOBJECT")
  (make-package "SSD::CLASSIFIEDOBJECT"))

(in-package "ROS")
;;//! \htmlinclude ClassifiedObject.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ssd::ClassifiedObject
  :super ros::object
  :slots (_header _score _label _bbox ))

(defmethod ssd::ClassifiedObject
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:score __score) 0.0)
    ((:label __label) "")
    ((:bbox __bbox) (instance ssd::BoundingBox :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _score (float __score))
   (setq _label (string __label))
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
   (&optional __label)
   (if __label (setq _label __label)) _label)
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
    ;; string _label
    4 (length _label)
    ;; ssd/BoundingBox _bbox
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
     ;; string _label
       (write-long (length _label) s) (princ _label s)
     ;; ssd/BoundingBox _bbox
       (send _bbox :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _score
     (setq _score (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; string _label
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _label (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; ssd/BoundingBox _bbox
     (send _bbox :deserialize buf ptr-) (incf ptr- (send _bbox :serialization-length))
   ;;
   self)
  )

(setf (get ssd::ClassifiedObject :md5sum-) "0b067c6fde340b0853980c4c9045f0cd")
(setf (get ssd::ClassifiedObject :datatype-) "ssd/ClassifiedObject")
(setf (get ssd::ClassifiedObject :definition-)
      "# A message representing an object that was classified using caffe.
Header header

# The certainty of the classification from 0 to 1
float64 score

# The label attached to this object
string label

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
MSG: ssd/BoundingBox
# A simple 2d bounding box message

float64 x_min
float64 y_min
float64 x_size
float64 y_size
")



(provide :ssd/ClassifiedObject "0b067c6fde340b0853980c4c9045f0cd")


