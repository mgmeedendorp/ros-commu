;; Auto-generated. Do not edit!


(when (boundp 'commu_wrapper::CommUUtter)
  (if (not (find-package "COMMU_WRAPPER"))
    (make-package "COMMU_WRAPPER"))
  (shadow 'CommUUtter (find-package "COMMU_WRAPPER")))
(unless (find-package "COMMU_WRAPPER::COMMUUTTER")
  (make-package "COMMU_WRAPPER::COMMUUTTER"))
(unless (find-package "COMMU_WRAPPER::COMMUUTTERREQUEST")
  (make-package "COMMU_WRAPPER::COMMUUTTERREQUEST"))
(unless (find-package "COMMU_WRAPPER::COMMUUTTERRESPONSE")
  (make-package "COMMU_WRAPPER::COMMUUTTERRESPONSE"))

(in-package "ROS")





(defclass commu_wrapper::CommUUtterRequest
  :super ros::object
  :slots (_utterance _blocking _english ))

(defmethod commu_wrapper::CommUUtterRequest
  (:init
   (&key
    ((:utterance __utterance) "")
    ((:blocking __blocking) nil)
    ((:english __english) nil)
    )
   (send-super :init)
   (setq _utterance (string __utterance))
   (setq _blocking __blocking)
   (setq _english __english)
   self)
  (:utterance
   (&optional __utterance)
   (if __utterance (setq _utterance __utterance)) _utterance)
  (:blocking
   (&optional __blocking)
   (if __blocking (setq _blocking __blocking)) _blocking)
  (:english
   (&optional __english)
   (if __english (setq _english __english)) _english)
  (:serialization-length
   ()
   (+
    ;; string _utterance
    4 (length _utterance)
    ;; bool _blocking
    1
    ;; bool _english
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _utterance
       (write-long (length _utterance) s) (princ _utterance s)
     ;; bool _blocking
       (if _blocking (write-byte -1 s) (write-byte 0 s))
     ;; bool _english
       (if _english (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _utterance
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _utterance (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _blocking
     (setq _blocking (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _english
     (setq _english (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass commu_wrapper::CommUUtterResponse
  :super ros::object
  :slots (_success ))

(defmethod commu_wrapper::CommUUtterResponse
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

(defclass commu_wrapper::CommUUtter
  :super ros::object
  :slots ())

(setf (get commu_wrapper::CommUUtter :md5sum-) "fc4efb8806f0415eaa9b069b92459024")
(setf (get commu_wrapper::CommUUtter :datatype-) "commu_wrapper/CommUUtter")
(setf (get commu_wrapper::CommUUtter :request) commu_wrapper::CommUUtterRequest)
(setf (get commu_wrapper::CommUUtter :response) commu_wrapper::CommUUtterResponse)

(defmethod commu_wrapper::CommUUtterRequest
  (:response () (instance commu_wrapper::CommUUtterResponse :init)))

(setf (get commu_wrapper::CommUUtterRequest :md5sum-) "fc4efb8806f0415eaa9b069b92459024")
(setf (get commu_wrapper::CommUUtterRequest :datatype-) "commu_wrapper/CommUUtterRequest")
(setf (get commu_wrapper::CommUUtterRequest :definition-)
      "
string utterance



bool blocking



bool english
---

bool success

")

(setf (get commu_wrapper::CommUUtterResponse :md5sum-) "fc4efb8806f0415eaa9b069b92459024")
(setf (get commu_wrapper::CommUUtterResponse :datatype-) "commu_wrapper/CommUUtterResponse")
(setf (get commu_wrapper::CommUUtterResponse :definition-)
      "
string utterance



bool blocking



bool english
---

bool success

")



(provide :commu_wrapper/CommUUtter "fc4efb8806f0415eaa9b069b92459024")


