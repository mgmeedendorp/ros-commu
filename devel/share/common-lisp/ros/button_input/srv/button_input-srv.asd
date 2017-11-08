
(cl:in-package :asdf)

(defsystem "button_input-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BinaryButtonInput" :depends-on ("_package_BinaryButtonInput"))
    (:file "_package_BinaryButtonInput" :depends-on ("_package"))
  ))