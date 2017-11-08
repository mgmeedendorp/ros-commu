;; Auto-generated. Do not edit!


(when (boundp 'button_input::BinaryButtonInput)
  (if (not (find-package "BUTTON_INPUT"))
    (make-package "BUTTON_INPUT"))
  (shadow 'BinaryButtonInput (find-package "BUTTON_INPUT")))
(unless (find-package "BUTTON_INPUT::BINARYBUTTONINPUT")
  (make-package "BUTTON_INPUT::BINARYBUTTONINPUT"))
(unless (find-package "BUTTON_INPUT::BINARYBUTTONINPUTREQUEST")
  (make-package "BUTTON_INPUT::BINARYBUTTONINPUTREQUEST"))
(unless (find-package "BUTTON_INPUT::BINARYBUTTONINPUTRESPONSE")
  (make-package "BUTTON_INPUT::BINARYBUTTONINPUTRESPONSE"))

(in-package "ROS")





(defclass button_input::BinaryButtonInputRequest
  :super ros::object
  :slots ())

(defmethod button_input::BinaryButtonInputRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass button_input::BinaryButtonInputResponse
  :super ros::object
  :slots (_response ))

(defmethod button_input::BinaryButtonInputResponse
  (:init
   (&key
    ((:response __response) 0)
    )
   (send-super :init)
   (setq _response (round __response))
   self)
  (:response
   (&optional __response)
   (if __response (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; uint8 _response
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _response
       (write-byte _response s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _response
     (setq _response (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass button_input::BinaryButtonInput
  :super ros::object
  :slots ())

(setf (get button_input::BinaryButtonInput :md5sum-) "59064532f110d857c53f36f4ab7ad30a")
(setf (get button_input::BinaryButtonInput :datatype-) "button_input/BinaryButtonInput")
(setf (get button_input::BinaryButtonInput :request) button_input::BinaryButtonInputRequest)
(setf (get button_input::BinaryButtonInput :response) button_input::BinaryButtonInputResponse)

(defmethod button_input::BinaryButtonInputRequest
  (:response () (instance button_input::BinaryButtonInputResponse :init)))

(setf (get button_input::BinaryButtonInputRequest :md5sum-) "59064532f110d857c53f36f4ab7ad30a")
(setf (get button_input::BinaryButtonInputRequest :datatype-) "button_input/BinaryButtonInputRequest")
(setf (get button_input::BinaryButtonInputRequest :definition-)
      "---
uint8 response
")

(setf (get button_input::BinaryButtonInputResponse :md5sum-) "59064532f110d857c53f36f4ab7ad30a")
(setf (get button_input::BinaryButtonInputResponse :datatype-) "button_input/BinaryButtonInputResponse")
(setf (get button_input::BinaryButtonInputResponse :definition-)
      "---
uint8 response
")



(provide :button_input/BinaryButtonInput "59064532f110d857c53f36f4ab7ad30a")


