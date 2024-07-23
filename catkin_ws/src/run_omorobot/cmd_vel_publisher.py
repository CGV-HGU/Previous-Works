#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def publish_cmd_vel():
    rospy.init_node('cmd_vel_publisher')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz

    while not rospy.is_shutdown():
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = 0.0
        cmd_vel_msg.angular.z = 0.0  
        pub.publish(cmd_vel_msg)
        print('linear velocity: ',cmd_vel_msg.linear.x,
              'angular velocity: ',cmd_vel_msg.angular.z)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_cmd_vel()
    except rospy.ROSInterruptException:
        pass