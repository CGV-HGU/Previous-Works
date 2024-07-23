#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

def bool_callback(msg):
    rospy.loginfo("Received boolean message: {}".format(msg.data))

def bool_subscriber():
    rospy.init_node("check_person_subscriber", anonymous=False)

    rospy.Subscriber('check_person', Bool, bool_callback)
    rospy.loginfo("Bool subscriber started.")

    rospy.spin()

if __name__ == '__main__':
    try:
        bool_subscriber()
    except rospy.ROSInterruptException:
        pass