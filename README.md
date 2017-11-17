# ros-commu
The catkin workspace folder for my commu dialogue project at Osaka University's Intelligent Robotics Laboratory

## Installation

### Install ROS

Install ROS kinetic, following the instructions on ROS wiki.

<http://wiki.ros.org/kinetic/Installation>

### Setup the catkin workspace

Clone this repository to a directory we'll refer to as `$CATKIN_WS`.

```shell
git clone --recursive https://github.com/seremis/ros-commu.git $CATKIN_WS
```

### Build the workspace

Build the necessary files by running `catkin_make` in the `$CATKIN_WS` directory and source the setup.bash file.

```shell
cd $CATKIN_WS
source /opt/ros/kinetic/setup.bash
catkin_make
source devel/setup.bash
```

### Run the dialogue package

Run the dialogue.launch file in the dialogue package by typing:

```shell
roslaunch dialogue dialogue.launch commu-ip:=192.168.1.1 commu-port:=6019 camera-path:=/dev/video0
```

The launch file accepts 3 arguments:
- `commu-ip` (default: 127.0.0.1):
  * The IP address of the CommU robot.
- `commu-port` (default: 6019): 
  * The port of the CommU manager program on the CommU.
- `camera-path` (default: /dev/fisheye-camera)
  * The path to the video device to use as input.