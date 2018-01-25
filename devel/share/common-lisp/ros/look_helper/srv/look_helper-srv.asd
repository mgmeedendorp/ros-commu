
(cl:in-package :asdf)

(defsystem "look_helper-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SetLookAtTarget" :depends-on ("_package_SetLookAtTarget"))
    (:file "_package_SetLookAtTarget" :depends-on ("_package"))
  ))