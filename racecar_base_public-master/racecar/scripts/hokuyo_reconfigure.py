#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import sys
import dynamic_reconfigure.client

ANGLE_MIN_VAL = -2.08621382713

if __name__ == '__main__':
	print 'created node'
	rospy.init_node('hokuyo_reconfigure', anonymous=True)
	print 'waiting for mesg'	
	msg = rospy.wait_for_message('/scan', LaserScan)
	if abs(msg.angle_min - ANGLE_MIN_VAL) > sys.float_info.epsilon:
		rospy.sleep(1.0)
		client = dynamic_reconfigure.client.Client('/laser_node')
		params = {'angle_min': ANGLE_MIN_VAL}
		config = client.update_configuration(params)
