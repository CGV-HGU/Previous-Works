#!/usr/bin/env python3

import rospy
import tf2_ros
from geometry_msgs.msg import TwistStamped, Twist

def tf_callback(msg):
    # 받은 변환 정보로부터 속도 정보를 추출하거나 변환합니다.
    # 여기에서는 간단히 변환 정보의 선속도를 cmd_vel에 적용하는 예제를 제
    cmd_vel_msg = Twist()
    cmd_vel_msg.linear.x = msg.twist.linear.x
    cmd_vel_msg.angular.z = msg.twist.angular.z

    # cmd_vel topic에 변환된 속도 정보 publish
    cmd_vel_pub.publish(cmd_vel_msg)

if __name__ == '__main__':
    rospy.init_node('tf_to_cmd_vel_node')

    # tf2 topic을 subscribe
    tf_topic = '/tf'
    rospy.loginfo("Subscribing to TF topic: %s", tf_topic)
    tf_sub = rospy.Subscriber(tf_topic, TwistStamped, tf_callback)

    # cmd_vel topic을 publish할 publisher 설정
    cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    rospy.spin()
