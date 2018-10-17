## INSTALLATION

Create a workspace if you do not have one already:
	
	cd ~
	mkdir -p <ws-name>/src
	cd ~/<ws-name>/src
	catkin_init_workspace

Clone this repo into a workspace: 

	cd ~/<ws-name>/src
	git clone https://gitlab.cs.washington.edu/uw_racecar/course_materials/racecar_base_public

Install ackermann_msgs and map_server:
	
	sudo apt-get install ros-kinetic-ackermann-msgs
	sudo apt-get install ros-kinetic-map-server

Install Cython:
	
	sudo pip install Cython

Install range_libc:

	cd ~/<ws_name>/src
	git clone https://github.com/kctess5/range_libc
	cd range_libc/pywrapper
	sudo python setup.py install

Merge in the repo's rosinstall:
	
	cd ~/<ws-name>/src
	wstool init
	wstool merge ./racecar_base_public/racecar-rviz-sim.rosinstall
	wstool up

Then build the worspace:
	
	cd ~/<ws_name>
	catkin_make

# Running the simulator
Make sure that the `racecar-version` parameter in racecar_base_public/racecar/launch/teleop.launch is set to `racecar-sim`. After sourcing your workspace, run `roslaunch racecar teleop.launch`. A small square gui will pop up - this window must be in focus in order to teleoperate the car in the next step.

Open rviz. Add a map topic. Under `Global Options`, make sure that the fixed frame is set to `map`. You may have to manually type it in. Click the `2D Pose Estimate` button near the center top of the rviz window. Then click and drag on the map to specify a starting pose for the car. Then add a pose topic that subscribes to `sim_car_pose/pose` and a laser scan topic that subscribes to `/scan`. You should now see a pose in the map representing the car and the corresponding laser scan.

You can move the car around using the wasd keys. Make sure that the small square gui that popped up when launching teleop.launch is in focus. The icon of this window in the Launcher Column of the Ubuntu UI should be a gray question mark. When you are done, first quit by pressing 'q', otherwise your keyboard might be left in a weird state. Then you can kill the nodes by pressing ctrl-c.

By default, the laser scan is noisy while the car pose is not. This can be adjusted by changing the parameter values in `racecar_base_public/racecar/launch/includes/racecar-sim/fake_urg_node.launch.xml` and `racecar_base_public/racecar/launch/includes/racecar-sim/sim_car_pose.launch.xml` as appropriate.
