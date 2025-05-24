# Argus Bot

Argus bot is a package that contains an autonomous ground vehicle described with ROS 2. 

## System Requirements

* Ubuntu 24

* ROS 2 Jazzy Jalisco

* Gazebo(not Gazebo classic)

## Local Setup

Create a workspace directory: 
```
mkdir dev_ws
```

Source the setup script(location may be different on your machine):
```
source /opt/ros/jazzy/setup.bash
```

Create a `src` sub directory to store packages in: 
```
mkdir dev_ws/src
```

Navigate into the `src` directory and clone this repository: 
```
git clone https://github.com/Max-Gabriel-Susman/argus_bot
```

Navigate back to the workspace root(`dev_ws`) and build it with `colcon` using the `symlink-install` setting: 
```
colcon build --symlink-install
```

Ensure `xacro` and `joint_state_publisher_gui` are installed:
```
sudo apt install ros-jazzy-xacro ros-jazzy-joint-state-publisher-gui
```

Source the workspace: 
```
source install/setup.bash
```

If you're launching without Gazebo(this method defaults to unix time): 
```
ros2 launch argus_bot rsp.launch.py
```

Otherwiseto manually launch with gazebo you need to use sim time:
```
ros2 launch argus_bot rsp.launch.py use_sim_time:=true
```

With Gazebo you'll need to make sure you have the bridge and Gazebo vendors installed: 
```
sudo apt install ros-jazzy-ros-gz
```

Open a second terminal, change directory into the package(`src/argus_bot`), and launch Gazebo: 
```
ros2 launch ros_gz_sim gz_sim.launch.py
```

At this point the Gazebo world launcher window should pop up. Make sure to select the `Empty` world template

Open a third window and spawn Argus Bot into the Gazebo instance: 
```
ros2 run ros_gz_sim create -topic robot_description -entity robot_name
```

## Manual Control

After local setup is performed(for Gazebo) initiate with: 
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```