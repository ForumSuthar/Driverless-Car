#!/usr/bin/env python

import rospy
import rosbag
from ackermann_msgs.msg import AckermannDriveStamped

BAG_TOPIC = '/vesc/low_level/ackermann_cmd_mux/input/teleop'# Name of the topic that should be extracted from the bag
PUB_TOPIC = '/vesc/high_level/ackermann_cmd_mux/input/nav_0'
PUB_RATE = 10# The rate at which messages should be published

# Loads a bag file, reads the msgs from the specified topic, and republishes them
def follow_bag(bag_path, follow_backwards):
	print bag_path
	pub = rospy.Publisher(PUB_TOPIC, AckermannDriveStamped ,queue_size = 1)	
	bag = rosbag.Bag(bag_path)
	rate = rospy.Rate(PUB_RATE)
   	for topic, msg, t in bag.read_messages(topics=[BAG_TOPIC]):
		bot = AckermannDriveStamped()
		bot.header.stamp = rospy.Time.now()
		bot.header.frame_id = '/map'
		bot.drive.steering_angle = msg.drive.steering_angle
		bot.drive.steering_angle_velocity = msg.drive.steering_angle_velocity
		if follow_backwards:
			bot.drive.speed = -msg.drive.speed
		else:
			bot.drive.speed = msg.drive.speed
		bot.drive.acceleration = msg.drive.acceleration
		bot.drive.jerk = msg.drive.jerk
		pub.publish(bot)
		rate.sleep()
   	bag.close()


if __name__ == '__main__':
	bag_path = "/home/car-user/racecar_AI/src/bagfile/figure8.bag" # The file path to the bag file

	follow_backwards = False # Whether or not the path should be followed backwards
	
	rospy.init_node('bag_follower', anonymous=True)
	bag_path = rospy.get_param("~bag_path", None)
	follow_backwards = rospy.get_param("~follow_backwards", None)
	
	# Populate param(s) with value(s) passed by launch file
	
	follow_bag(bag_path, follow_backwards)

	rospy.spin()
