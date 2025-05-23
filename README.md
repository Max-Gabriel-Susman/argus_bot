# Argus Bot

Argus bot is a package that contains an autonomous ground vehicle described with ROS 2. 

## System Requirements

* Ubuntu 24

* ROS 2 Jazzy Jalisco

## Local Setup

Create a workspace directory: 
```
mkdir dev_ws
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

Launch: 
```
ros2 launch argus_bot rsp.launch.py
```

