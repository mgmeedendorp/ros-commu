;; Auto-generated. Do not edit!


(when (boundp 'commu_wrapper::CommULook)
  (if (not (find-package "COMMU_WRAPPER"))
    (make-package "COMMU_WRAPPER"))
  (shadow 'CommULook (find-package "COMMU_WRAPPER")))
(unless (find-package "COMMU_WRAPPER::COMMULOOK")
  (make-package "COMMU_WRAPPER::COMMULOOK"))
(unless (find-package "COMMU_WRAPPER::COMMULOOKREQUEST")
  (make-package "COMMU_WRAPPER::COMMULOOKREQUEST"))
(unless (find-package "COMMU_WRAPPER::COMMULOOKRESPONSE")
  (make-package "COMMU_WRAPPER::COMMULOOKRESPONSE"))

(in-package "ROS")





(defclass commu_wrapper::CommULookRequest
  :super ros::object
  :slots (_look_x _look_y _look_z ))

(defmethod commu_wrapper::CommULookRequest
  (:init
   (&key
    ((:look_x __look_x) 0)
    ((:look_y __look_y) 0)
    ((:look_z __look_z) 0)
    )
   (send-super :init)
   (setq _look_x (round __look_x))
   (setq _look_y (round __look_y))
   (setq _look_z (round __look_z))
   self)
  (:look_x
   (&optional __look_x)
   (if __look_x (setq _look_x __look_x)) _look_x)
  (:look_y
   (&optional __look_y)
   (if __look_y (setq _look_y __look_y)) _look_y)
  (:look_z
   (&optional __look_z)
   (if __look_z (setq _look_z __look_z)) _look_z)
  (:serialization-length
   ()
   (+
    ;; int32 _look_x
    4
    ;; int32 _look_y
    4
    ;; int32 _look_z
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _look_x
       (write-long _look_x s)
     ;; int32 _look_y
       (write-long _look_y s)
     ;; int32 _look_z
       (write-long _look_z s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _look_x
     (setq _look_x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _look_y
     (setq _look_y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _look_z
     (setq _look_z (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass commu_wrapper::CommULookResponse
  :super ros::object
  :slots (_success ))

(defmethod commu_wrapper::CommULookResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass commu_wrapper::CommULook
  :super ros::object
  :slots ())

(setf (get commu_wrapper::CommULook :md5sum-) "586b9328c974a82a91e07618b791be94")
(setf (get commu_wrapper::CommULook :datatype-) "commu_wrapper/CommULook")
(setf (get commu_wrapper::CommULook :request) commu_wrapper::CommULookRequest)
(setf (get commu_wrapper::CommULook :response) commu_wrapper::CommULookResponse)

(defmethod commu_wrapper::CommULookRequest
  (:response () (instance commu_wrapper::CommULookResponse :init)))

(setf (get commu_wrapper::CommULookRequest :md5sum-) "586b9328c974a82a91e07618b791be94")
(setf (get commu_wrapper::CommULookRequest :datatype-) "commu_wrapper/CommULookRequest")
(setf (get commu_wrapper::CommULookRequest :definition-)
      "



int32 look_x


int32 look_y


int32 look_z

---


bool success
")

(setf (get commu_wrapper::CommULookResponse :md5sum-) "586b9328c974a82a91e07618b791be94")
(setf (get commu_wrapper::CommULookResponse :datatype-) "commu_wrapper/CommULookResponse")
(setf (get commu_wrapper::CommULookResponse :definition-)
      "



int32 look_x


int32 look_y


int32 look_z

---


bool success
")



(provide :commu_wrapper/CommULook "586b9328c974a82a91e07618b791be94")


