roscore

rosrun usb_cam usb_cam_node



rosrun image_transport republish raw in:=/usb_cam/image_raw raw out:=/camera/image_raw

rosrun stella_vslam_ros run_slam -i /home/cgvlab/lib/stella_vslam/build/oseok_4_1_ver1.msg --disable-mapping -v /home/cgvlab/lib/stella_vslam/build/orb_vocab.fbow -c /home/cgvlab/lib/stella_vslam/example/usb_webcam.yaml

rosrun image_transport republish raw in:=/videofile/image_raw raw out:=/camera/image_raw
