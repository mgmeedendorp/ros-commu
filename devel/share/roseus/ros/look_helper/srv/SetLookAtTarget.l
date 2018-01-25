;; Auto-generated. Do not edit!


(when (boundp 'look_helper::SetLookAtTarget)
  (if (not (find-package "LOOK_HELPER"))
    (make-package "LOOK_HELPER"))
  (shadow 'SetLookAtTarget (find-package "LOOK_HELPER")))
(unless (find-package "LOOK_HELPER::SETLOOKATTARGET")
  (make-package "LOOK_HELPER::SETLOOKATTARGET"))
(unless (find-package "LOOK_HELPER::SETLOOKATTARGETREQUEST")
  (make-package "LOOK_HELPER::SETLOOKATTARGETREQUEST"))
(unless (find-package "LOOK_HELPER::SETLOOKATTARGETRESPONSE")
  (make-package "LOOK_HELPER::SETLOOKATTARGETRESPONSE"))

(in-package "ROS")





(defclass look_helper::SetLookAtTargetRequest
  :super ros::object
  :slots (_target_frame_name ))

(defmethod look_helper::SetLookAtTargetRequest
  (:init
   (&key
    ((:target_frame_name __target_frame_name) "")
    )
   (send-super :init)
   (setq _target_frame_name (string __target_frame_name))
   self)
  (:target_frame_name
   (&optional __target_frame_name)
   (if __target_frame_name (setq _target_frame_name __target_frame_name)) _target_frame_name)
  (:serialization-length
   ()
   (+
    ;; string _target_frame_name
    4 (length _target_frame_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _target_frame_name
       (write-long (length _target_frame_name) s) (princ _target_frame_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _target_frame_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _target_frame_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass look_helper::SetLookAtTargetResponse
  :super ros::object
  :slots (_success ))

(defmethod look_helper::SetLookAtTargetResponse
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

(defclass look_helper::SetLookAtTarget
  :super ros::object
  :slots ())

(setf (get look_helper::SetLookAtTarget :md5sum-) "1030478efebc9e6deae2c1ba1ffff144")
(setf (get look_helper::SetLookAtTarget :datatype-) "look_helper/SetLookAtTarget")
(setf (get look_helper::SetLookAtTarget :request) look_helper::SetLookAtTargetRequest)
(setf (get look_helper::SetLookAtTarget :response) look_helper::SetLookAtTargetResponse)

(defmethod look_helper::SetLookAtTargetRequest
  (:response () (instance look_helper::SetLookAtTargetResponse :init)))

(setf (get look_helper::SetLookAtTargetRequest :md5sum-) "1030478efebc9e6deae2c1ba1ffff144")
(setf (get look_helper::SetLookAtTargetRequest :datatype-) "look_helper/SetLookAtTargetRequest")
(setf (get look_helper::SetLookAtTargetRequest :definition-)
      "


string target_frame_name

---


bool success
")

(setf (get look_helper::SetLookAtTargetResponse :md5sum-) "1030478efebc9e6deae2c1ba1ffff144")
(setf (get look_helper::SetLookAtTargetResponse :datatype-) "look_helper/SetLookAtTargetResponse")
(setf (get look_helper::SetLookAtTargetResponse :definition-)
      "


string target_frame_name

---


bool success
")



(provide :look_helper/SetLookAtTarget "1030478efebc9e6deae2c1ba1ffff144")


