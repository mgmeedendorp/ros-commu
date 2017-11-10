
(cl:in-package :asdf)

(defsystem "ssd-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BoundingBox" :depends-on ("_package_BoundingBox"))
    (:file "_package_BoundingBox" :depends-on ("_package"))
    (:file "ClassifiedObject" :depends-on ("_package_ClassifiedObject"))
    (:file "_package_ClassifiedObject" :depends-on ("_package"))
    (:file "ClassifiedObjectArray" :depends-on ("_package_ClassifiedObjectArray"))
    (:file "_package_ClassifiedObjectArray" :depends-on ("_package"))
  ))