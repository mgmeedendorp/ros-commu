
(cl:in-package :asdf)

(defsystem "commu_wrapper-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "CommULook" :depends-on ("_package_CommULook"))
    (:file "_package_CommULook" :depends-on ("_package"))
    (:file "CommUUtter" :depends-on ("_package_CommUUtter"))
    (:file "_package_CommUUtter" :depends-on ("_package"))
  ))