#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped
import Utils # <----------- LOOK AT THESE FUNCTIONS ***************************

SUB_TOPIC = '/sim_car_pose/pose' # The topic that provides the simulated car pose
PUB_TOPIC = '/clone_follower_pose/pose' # The topic that you should publish to
MAP_TOPIC = 'static_map' # The service topic that will provide the map

# Follows the simulated robot around
class CloneFollower:

  '''
  Initializes a CloneFollower object
  In:
    follow_offset: The required x offset between the robot and its clone follower
    force_in_bounds: Whether the clone should toggle between following in front
                     and behind when it goes out of bounds of the map
  '''
  def __init__(self, follow_offset, force_in_bounds):
    # YOUR CODE HERE 
    self.follow_offset = follow_offset# Store the input params in self
    self.force_in_bounds = force_in_bounds # Store the input params in self
    self.map_img, self.map_info = Utils.get_map(MAP_TOPIC)# Get and store the map
                                  # for bounds checking
    
    # Setup publisher that publishes to PUB_TOPIC
    self.pub = rospy.Publisher(PUB_TOPIC, PoseStamped ,queue_size = 1)
    
    # Setup subscriber that subscribes to SUB_TOPIC and uses the self.update_pose
    # callback
    self.sub = rospy.Subscriber(SUB_TOPIC, PoseStamped, self.update_pose, queue_size = 1)
    
  '''
  Given the translation and rotation between the robot and map, computes the pose
  of the clone
  (This function is optional)
  In:
    trans: The translation between the robot and map
    rot: The rotation between the robot and map
  Out:
    The pose of the clone
  '''
  def compute_follow_pose(self, trans, rot):
	
    # YOUR CODE HERE
	pass
    
  '''
  Callback that runs each time a sim pose is received. Should publish an updated
  pose of the clone.
  In:
    msg: The pose of the simulated car. Should be a geometry_msgs/PoseStamped
  '''  
  def update_pose(self, msg):

    # YOUR CODE HERE
    # Compute the pose of the clone
    # Note: To convert from a message quaternion to corresponding rotation matrix,
    #       look at the functions in Utils.py
	posAx = msg.pose.position.x
	posAy = msg.pose.position.y
	posAquaternion = msg.pose.orientation
	angleA = Utils.quaternion_to_angle(posAquaternion)
	posTx = self.follow_offset*np.cos(angleA)
	posTy = self.follow_offset*np.sin(angleA)
	print Utils.rotation_matrix(angleA)
	posBMatrix = np.array(np.matmul(Utils.rotation_matrix(0),[[posAx],[posAy]]))+np.array([[posTx],[posTy]])

    # Check bounds if required
	if self.force_in_bounds:
      # Functions in Utils.py will again be useful here
		posBArray = [posBMatrix[0], posBMatrix[1], angleA]
		print posBMatrix
		posBOnMap = Utils.world_to_map(posBArray, self.map_info)
		if self.map_img[posBOnMap[0],posBOnMap[1]]:
			pass
		else:
			self.follow_offset = -self.follow_offset
			posTx = self.follow_offset*np.cos(angleA)
			posTy = self.follow_offset*np.sin(angleA)
			posBMatrix = np.array(np.matmul(Utils.rotation_matrix(0),[[posAx],[posAy]]))+np.array([[posTx],[posTy]])
      
    # Setup the out going PoseStamped message
	posB = PoseStamped()
	posB.header.stamp = rospy.Time.now()
	posB.header.frame_id = '/map'
	posB.pose.position.x = posBMatrix[0]
	posB.pose.position.y = posBMatrix[1]
	posB.pose.position.z = 0
	
	posB.pose.orientation = posAquaternion

    # Publish the clone's pose
	self.pub.publish(posB)
      
    
if __name__ == '__main__':
  follow_offset = 1.5 # The offset between the robot and clone
  force_in_bounds = True # Whether or not map bounds should be enforced
  
  rospy.init_node('clone_follower', anonymous=True) # Initialize the node
  
  # Populate params with values passed by launch file
  follow_offset = rospy.get_param("~follow_offset", None)# YOUR CODE HERE
  force_in_bounds = rospy.get_param("~force_in_bounds",None)# YOUR CODE HERE
  
  cf = CloneFollower(follow_offset, force_in_bounds) # Create a clone follower
  rospy.spin() # Spin
  
