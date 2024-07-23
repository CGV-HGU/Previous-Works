#!/usr/bin/env python3

import rospy
import numpy as np
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Vector3, PoseWithCovarianceStamped, Point, Quaternion
import geometry_msgs
import cv2
import tf

# pip install transforms3d
import transforms3d

## /initialpose echo result : 
# header:
#   seq: 4
#   stamp:
#     secs: 1714978216
#     nsecs: 615329675
#   frame_id: "world"
# pose:
#   pose:
#     position:
#       x: 350.7293701171875
#       y: 383.0067443847656
#       z: 0.0
#     orientation:
#       x: 0.0
#       y: 0.0
#       z: 0.0
#       w: 1.0
#   covariance: [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853892326654787]



# 3D -> 2D 변환 함수
def transform_3d_to_2d(point_3d, scale_factor, grid_min, grid_max):
    norm_x = ((grid_max[0] - grid_min[0]) - 1) / (grid_max[0] - grid_min[0])
    norm_z = ((grid_max[1] - grid_min[1]) - 1) / (grid_max[1] - grid_min[1])
    x = int((np.floor(point_3d[0] * scale_factor) - grid_min[0]) * norm_x)
    z = int((np.floor(point_3d[2] * scale_factor) - grid_min[1]) * norm_z)
    return (x, z)


def camera_pose_callback(msg):
    # 현재 카메라 3D 포즈 정보 로깅
    # rospy.loginfo(f"Received camera pose: Position (x: {-msg.pose.pose.position.y}, y: {-msg.pose.pose.position.z}, z: {msg.pose.pose.position.x})")
    # rospy.loginfo(f"Received camera pose: Quaternion (x: {msg.pose.pose.orientation.x}, y: {msg.pose.pose.orientation.y}, z: {msg.pose.pose.orientation.z}, w: {msg.pose.pose.orientation.w})")
    # 3D 좌표를 2D로 변환

    #############################################
    #### first map -> map.png ####
    #### file name -> 0123    ####
    '''
    scale_factor = 10 # 스케일 인자
    grid_min = (-163, -361) # 그리드 최소값
    grid_max = (221, 377) # 그리드 최대값
    '''
    #############################################

    #############################################
    #### second map -> map_oh_0314_1_scale_30.png
    #### file name  -> 0314_1_more_keyfrm
    '''
    scale_factor = 30
    grid_min = (-620, -738)
    grid_max = (266, 411)
    '''
    #############################################

    #############################################
    #### map_0429.jpg
    #### file name  -> oh_4f_0429
    
    scale_factor = 50
    grid_min = (-175, -331)
    grid_max = (375, 569)
    
    #############################################
    
    point_3d = (-msg.pose.pose.position.y, -msg.pose.pose.position.z, msg.pose.pose.position.x)
    point_2d = transform_3d_to_2d(point_3d, scale_factor, grid_min, grid_max)

    # 변환된 2D 좌표 로깅
    rospy.loginfo(f"Transformed 2D position: (x: {point_2d[1]}, y: {point_2d[0]})")
    
    # map_val =  1000 / 2
    map_val = 978 // 2
    rate = rospy.Rate(0.0001)
    # while not rospy.is_shutdown():
    new_msg = PoseWithCovarianceStamped()
    
    new_msg.header.seq = -1
    new_msg.header.stamp = rospy.Time.now()
    new_msg.header.frame_id = "world"

    new_msg.pose.pose.position = Point(point_2d[1], map_val-point_2d[0], 0.0)

    # m = msg.pose.pose.orientation
    # e = tf.transformations.euler_from_quaternion([m.x, m.y, m.z, m.w])
    # q = tf.transformations.quaternion_from_euler(e[0], 0, 0)
    # new_msg.pose.pose.orientation = q

    new_msg.pose.pose.orientation = Quaternion(0, 0, 0, 1)
    

    new_msg.pose.covariance = [0] * 36 # initialize array with 36 zeros
    new_msg.pose.covariance[0] = 0.25
    new_msg.pose.covariance[7] = 0.25
    new_msg.pose.covariance[35] = 0.06853892326654787

    # rostopic pub --once /initialpose geometry_msgs/PoseWithCovarianceStamped '{header: {seq: 0, stamp: now, frame_id: "world"}, pose: {pose: {position: {x: 300.0, y: 383.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}, covariance: [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853892326654787]}}'

    # rostopic pub --once /move_base_simple/goal geometry_msgs/PoseStamped "{header: {seq: 0, stamp: now, frame_id: 'world'}, pose: {position: {x: 500.0, y: 383.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}"

    # angle = transforms3d.euler.quat2euler([msg.pose.pose.orientation.w, msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z], axes='sxyz')
    # yaw = angle[2] - 3.14/4 # need normalization???
    # rospy.loginfo(f"Transformed yaw: (z: {yaw})")
    # new_msg.z = yaw

    init_pose.publish(new_msg)
    # rate.sleep()

    # while True:
    #     pass



def camera_pose_listener():
    # ROS 노드 초기화
    rospy.init_node('camera_pose_subscriber_node', anonymous=True)

    # '/run_slam/camera_pose' 토픽 구독
    rospy.Subscriber('/run_slam/camera_pose', Odometry, camera_pose_callback)

    # 프로그램 유지
    rospy.spin()

if __name__ == '__main__':
    try:
        init_pose = rospy.Publisher('initialpose', PoseWithCovarianceStamped, queue_size=10)
        camera_pose_listener()
    except rospy.ROSInterruptException:
        pass