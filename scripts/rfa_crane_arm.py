#!/usr/bin/env python

"""
    crane_arm.py - move crane arm according to predefined gestures

"""

import rospy
from std_msgs.msg import Float64

class Loop:
    def __init__(self):
        rospy.on_shutdown(self.cleanup)

	# publish command message to joints/servos of arm
    	self.joint1 = rospy.Publisher('/arm_shoulder_pan_joint/command',Float64)
	self.joint2 = rospy.Publisher('/arm_shoulder_lift_joint/command',Float64)
    	self.joint3 = rospy.Publisher('/arm_elbow_flex_joint/command',Float64)
    	self.joint4 = rospy.Publisher('/arm_wrist_flex_joint/command',Float64)
	self.joint5 = rospy.Publisher('/gripper_joint/command',Float64)
	self.pos1 = Float64()
    	self.pos2 = Float64()
    	self.pos3 = Float64()
    	self.pos4 = Float64()
    	self.pos5 = Float64()
	rospy.sleep(3)
	
	# Arm in "home" position
	self.pos1 = 0.000
	self.pos2 = -1.658
	self.pos3 = -2.88
	self.pos4 = -1.01
	self.pos5 = 0.000
	self.joint1.publish(self.pos1)
	self.joint2.publish(self.pos2)
	self.joint3.publish(self.pos3)
	self.joint4.publish(self.pos4)
	self.joint5.publish(self.pos5)
	rospy.sleep(3)

	self.pos1 = 0.000
	self.pos2 = 0.902
	self.pos3 = -1.892
	self.pos4 = -0.436
	self.pos5 = -0.523
	self.joint1.publish(self.pos1)
	self.joint2.publish(self.pos2)
	self.joint3.publish(self.pos3)
	self.joint4.publish(self.pos4)
	self.joint5.publish(self.pos5)
	rospy.sleep(1)

	self.pos4 = 1.57
	self.joint4.publish(self.pos4)
	rospy.sleep(1)

	self.pos1 = 0.000
	self.pos2 = 1.745
	self.pos3 = -1.57
	self.joint1.publish(self.pos1)
	self.joint2.publish(self.pos2)
	self.joint3.publish(self.pos3)
	rospy.sleep(2)	

	self.pos1 = 0.000
	self.pos2 = 1.745
	self.pos3 = -1.05
	self.pos4 = 1.178
	self.pos5 = -0.523
	self.joint1.publish(self.pos1)
	self.joint2.publish(self.pos2)
	self.joint3.publish(self.pos3)
	self.joint4.publish(self.pos4)
	self.joint5.publish(self.pos5)
	rospy.sleep(1)

	self.pos5 = 0.48
	self.joint5.publish(self.pos5)
	rospy.sleep(2)

	self.pos1 = 0.000
	self.pos2 = -0.9265
	self.pos3 = -2.387
	self.pos5 = 0.48
	self.joint1.publish(self.pos1)
	self.joint2.publish(self.pos2)
	self.joint3.publish(self.pos3)
	self.joint5.publish(self.pos5)
	rospy.sleep(1)
		
	self.pos4 = -0.30
	self.joint4.publish(self.pos4)
	rospy.sleep(2)

    def cleanup(self):
        rospy.loginfo("Shutting down crane arm....")

if __name__=="__main__":
    rospy.init_node('crane_arm')
    try:
        Loop()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

