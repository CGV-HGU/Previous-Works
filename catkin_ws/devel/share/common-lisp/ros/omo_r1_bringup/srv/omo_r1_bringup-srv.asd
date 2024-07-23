
(cl:in-package :asdf)

(defsystem "omo_r1_bringup-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ResetOdom" :depends-on ("_package_ResetOdom"))
    (:file "_package_ResetOdom" :depends-on ("_package"))
  ))