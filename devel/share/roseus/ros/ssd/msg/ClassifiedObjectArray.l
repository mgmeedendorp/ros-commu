;; Auto-generated. Do not edit!


(when (boundp 'ssd::ClassifiedObjectArray)
  (if (not (find-package "SSD"))
    (make-package "SSD"))
  (shadow 'ClassifiedObjectArray (find-package "SSD")))
(unless (find-package "SSD::CLASSIFIEDOBJECTARRAY")
  (make-package "SSD::CLASSIFIEDOBJECTARRAY"))

(in-package "ROS")
;;//! \htmlinclude ClassifiedObjectArray.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass ssd::ClassifiedObjectArray
  :super ros::object
  :slots (_objects _image ))

(defmethod ssd::ClassifiedObjectArray
  (:init
   (&key
    ((:objects __objects) (let (r) (dotimes (i 0) (push (instance ssd::ClassifiedObject :init) r)) r))
    ((:image __image) (instance sensor_msgs::Image :init))
    )
   (send-super :init)
   (setq _objects __objects)
   (setq _image __image)
   self)
  (:objects
   (&rest __objects)
   (if (keywordp (car __objects))
       (send* _objects __objects)
     (progn
       (if __objects (setq _objects (car __objects)))
       _objects)))
  (:image
   (&rest __image)
   (if (keywordp (car __image))
       (send* _image __image)
     (progn
       (if __image (setq _image (car __image)))
       _image)))
  (:serialization-length
   ()
   (+
    ;; ssd/ClassifiedObject[] _objects
    (apply #'+ (send-all _objects :serialization-length)) 4
    ;; sensor_msgs/Image _image
    (send _image :serialization-length)
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
     ;; sensor_msgs/Image _image
       (send _image :serialize s)
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
   ;; sensor_msgs/Image _image
     (send _image :deserialize buf ptr-) (incf ptr- (send _image :serialization-length))
   ;;
   self)
  )

(setf (get ssd::ClassifiedObjectArray :md5sum-) "ccc40aeeae1ee53272e491b81bf276de")
(setf (get ssd::ClassifiedObjectArray :datatype-) "ssd/ClassifiedObjectArray")
(setf (get ssd::ClassifiedObjectArray :definition-)
      "# An array of ClassifiedObject messages

ClassifiedObject[] objects

#The classified image
sensor_msgs/Image image
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
================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

")



(provide :ssd/ClassifiedObjectArray "ccc40aeeae1ee53272e491b81bf276de")


