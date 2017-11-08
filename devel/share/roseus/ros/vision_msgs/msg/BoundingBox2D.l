;; Auto-generated. Do not edit!


(when (boundp 'vision_msgs::BoundingBox2D)
  (if (not (find-package "VISION_MSGS"))
    (make-package "VISION_MSGS"))
  (shadow 'BoundingBox2D (find-package "VISION_MSGS")))
(unless (find-package "VISION_MSGS::BOUNDINGBOX2D")
  (make-package "VISION_MSGS::BOUNDINGBOX2D"))

(in-package "ROS")
;;//! \htmlinclude BoundingBox2D.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass vision_msgs::BoundingBox2D
  :super ros::object
  :slots (_center _size_x _size_y ))

(defmethod vision_msgs::BoundingBox2D
  (:init
   (&key
    ((:center __center) (instance geometry_msgs::Pose2D :init))
    ((:size_x __size_x) 0.0)
    ((:size_y __size_y) 0.0)
    )
   (send-super :init)
   (setq _center __center)
   (setq _size_x (float __size_x))
   (setq _size_y (float __size_y))
   self)
  (:center
   (&rest __center)
   (if (keywordp (car __center))
       (send* _center __center)
     (progn
       (if __center (setq _center (car __center)))
       _center)))
  (:size_x
   (&optional __size_x)
   (if __size_x (setq _size_x __size_x)) _size_x)
  (:size_y
   (&optional __size_y)
   (if __size_y (setq _size_y __size_y)) _size_y)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose2D _center
    (send _center :serialization-length)
    ;; float64 _size_x
    8
    ;; float64 _size_y
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose2D _center
       (send _center :serialize s)
     ;; float64 _size_x
       (sys::poke _size_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _size_y
       (sys::poke _size_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose2D _center
     (send _center :deserialize buf ptr-) (incf ptr- (send _center :serialization-length))
   ;; float64 _size_x
     (setq _size_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _size_y
     (setq _size_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get vision_msgs::BoundingBox2D :md5sum-) "9ab41e2a4c8627735e5091a9abd68b02")
(setf (get vision_msgs::BoundingBox2D :datatype-) "vision_msgs/BoundingBox2D")
(setf (get vision_msgs::BoundingBox2D :definition-)
      "# A 2D bounding box that can be rotated about its center.
# All dimensions are in pixels, but represented using floating-point
#   values to allow sub-pixel precision. If an exact pixel crop is required
#   for a rotated bounding box, it can be calculated using Bresenham's line
#   algorithm.

# The 2D position (in pixels) and orientation of the bounding box center.
geometry_msgs/Pose2D center

# The size (in pixels) of the bounding box surrounding the object relative 
# to the pose of its center.
float64 size_x
float64 size_y

================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
float64 theta
")



(provide :vision_msgs/BoundingBox2D "9ab41e2a4c8627735e5091a9abd68b02")


