;; Auto-generated. Do not edit!


(when (boundp 'ssd::ClassifiedObjectArray)
  (if (not (find-package "SSD"))
    (make-package "SSD"))
  (shadow 'ClassifiedObjectArray (find-package "SSD")))
(unless (find-package "SSD::CLASSIFIEDOBJECTARRAY")
  (make-package "SSD::CLASSIFIEDOBJECTARRAY"))

(in-package "ROS")
;;//! \htmlinclude ClassifiedObjectArray.msg.html


(defclass ssd::ClassifiedObjectArray
  :super ros::object
  :slots (_objects ))

(defmethod ssd::ClassifiedObjectArray
  (:init
   (&key
    ((:objects __objects) (let (r) (dotimes (i 0) (push (instance ssd::ClassifiedObject :init) r)) r))
    )
   (send-super :init)
   (setq _objects __objects)
   self)
  (:objects
   (&rest __objects)
   (if (keywordp (car __objects))
       (send* _objects __objects)
     (progn
       (if __objects (setq _objects (car __objects)))
       _objects)))
  (:serialization-length
   ()
   (+
    ;; ssd/ClassifiedObject[] _objects
    (apply #'+ (send-all _objects :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; ssd/ClassifiedObject[] _objects
     (write-long (length _objects) s)
     (dolist (elem _objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; ssd/ClassifiedObject[] _objects
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _objects (let (r) (dotimes (i n) (push (instance ssd::ClassifiedObject :init) r)) r))
     (dolist (elem- _objects)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ssd::ClassifiedObjectArray :md5sum-) "59f286ee6aa871e16584f755f2af5a21")
(setf (get ssd::ClassifiedObjectArray :datatype-) "ssd/ClassifiedObjectArray")
(setf (get ssd::ClassifiedObjectArray :definition-)
      "# An array of ClassifiedObject messages

ClassifiedObject[] objects
================================================================================
MSG: ssd/ClassifiedObject
# A message representing an object that was classified using caffe.
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



(provide :ssd/ClassifiedObjectArray "59f286ee6aa871e16584f755f2af5a21")


