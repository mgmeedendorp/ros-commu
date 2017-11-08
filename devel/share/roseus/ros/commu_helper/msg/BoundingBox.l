;; Auto-generated. Do not edit!


(when (boundp 'commu_helper::BoundingBox)
  (if (not (find-package "COMMU_HELPER"))
    (make-package "COMMU_HELPER"))
  (shadow 'BoundingBox (find-package "COMMU_HELPER")))
(unless (find-package "COMMU_HELPER::BOUNDINGBOX")
  (make-package "COMMU_HELPER::BOUNDINGBOX"))

(in-package "ROS")
;;//! \htmlinclude BoundingBox.msg.html


(defclass commu_helper::BoundingBox
  :super ros::object
  :slots (_x_min _y_min _x_size _y_size ))

(defmethod commu_helper::BoundingBox
  (:init
   (&key
    ((:x_min __x_min) 0.0)
    ((:y_min __y_min) 0.0)
    ((:x_size __x_size) 0.0)
    ((:y_size __y_size) 0.0)
    )
   (send-super :init)
   (setq _x_min (float __x_min))
   (setq _y_min (float __y_min))
   (setq _x_size (float __x_size))
   (setq _y_size (float __y_size))
   self)
  (:x_min
   (&optional __x_min)
   (if __x_min (setq _x_min __x_min)) _x_min)
  (:y_min
   (&optional __y_min)
   (if __y_min (setq _y_min __y_min)) _y_min)
  (:x_size
   (&optional __x_size)
   (if __x_size (setq _x_size __x_size)) _x_size)
  (:y_size
   (&optional __y_size)
   (if __y_size (setq _y_size __y_size)) _y_size)
  (:serialization-length
   ()
   (+
    ;; float64 _x_min
    8
    ;; float64 _y_min
    8
    ;; float64 _x_size
    8
    ;; float64 _y_size
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x_min
       (sys::poke _x_min (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_min
       (sys::poke _y_min (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _x_size
       (sys::poke _x_size (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y_size
       (sys::poke _y_size (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x_min
     (setq _x_min (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_min
     (setq _y_min (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _x_size
     (setq _x_size (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y_size
     (setq _y_size (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get commu_helper::BoundingBox :md5sum-) "49841939163c4125050016679dd0cb15")
(setf (get commu_helper::BoundingBox :datatype-) "commu_helper/BoundingBox")
(setf (get commu_helper::BoundingBox :definition-)
      "# A simple 2d bounding box message

float64 x_min
float64 y_min
float64 x_size
float64 y_size
")



(provide :commu_helper/BoundingBox "49841939163c4125050016679dd0cb15")


