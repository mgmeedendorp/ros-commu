# ros-commu
The catkin workspace folder for my commu dialogue project at Osaka University's Intelligent Robotics Laboratory

More information about the SoTa / CommU robot used can be found at [CommU.md](CommU.md).

## Exploring this repository

This repository might seem quite messy to someone unfamilliar with ROS. My main advice is to work through the ROS tutorials on the project structure and start exploring this project by looking at the `src/dialogue/dialogue.launch` file.

## Installation

### Requirements
This system uses 3 devices connected to the same network. One of them is an Intel Euclid Development Kit, used as a ROS master, a CommU-compatible robot, such as a Sota, and the other is a beefy pc with a GPU to run the Single-Shot Multibox Detector neural network, which is used to classify images.

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
rosdep install cv_camera
catkin_make
source devel/setup.bash
```

### Install caffe

Install caffe using the instructions at <https://github.com/weiliu89/caffe/blob/ssd/README.md>. 

Set the `$CATKIN_WS/src/ssd/caffe/` directory as the `$CAFFE_ROOT` environment variable.

```shell
export CAFFE_ROOT=$CATKIN_WS/src/ssd/caffe/
```

Follow the instructions under 'Installation' and then either download the pre-trained model (as specified under step 1 of 'Train/Eval') or train your own model by following the steps under 'Preparation' and 'Train/Eval'

Then append the `$CAFFE_ROOT/python` directory to `PYTHONPATH`:

```shell
export PYTHONPATH = $PYTHONPATH:$CAFFE_ROOT/python
```

### Configure ROS on the euclid and the gpu-pc
Follow the following guide on the ROS wiki to configure the network on both devices: <http://wiki.ros.org/ROS/Tutorials/MultipleMachines>.

Either configure the hostname of the euclid to be `EUCLID_70FD` (not recommended) or pass the `euclid:=<euclid hostname>` argument to the launch file.

### Run the dialogue package

Run the dialogue.launch file in the dialogue package by typing:

```shell
roslaunch dialogue dialogue.launch commu-ip:=192.168.1.1 commu-port:=6001 camera-path:=/dev/video0
```

The launch file accepts 8 arguments:
- `commu-ip` (required):
  * The IP address of the CommU robot.
- `commu-port` (default: 6001): 
  * The port of the CommU manager program on the CommU.
- `commu-volume` (default: 10):
  * The volume of the speech on the CommU (from 0 to 100).
- `debug-mode` (default: true):
  * Whether to run the commu_wrapper package in debug mode. Debug mode opens a window with the live camera footage from 
  the `camera-path` parameter and illustrates what objects are recognized on the image. It also displays what the CommU
  is currently saying.
- `classification-topic` (default: "/ssd_node/classification_result") 
  * This argument can be used to specify an alternate object classification topic. For this the default covers almost 
  all possible use cases.  
- `camera-path` (default: /dev/fisheye-camera):
  * The path to the video device to use as input. The video device has to be connected to the GPU-pc. It is also possible to use another camera, by remapping the raw output topic of the camera to `/cv_camera/image_raw`.
- `euclid` (default: EUCLID_70FD):  
  * The hostname of the Intel Euclid Development Kit device.


### Setting camera position parameters
There are also 12 other parameters which can't be passed via the launch file. These are the Euclid and webcam camera position parameters of the `look_helper` package. The Euclid is used for person detection and the webcam for object classification. The coordinates are required to provide their offsets and rotations from the robot. These parameters are:

- `look_helper/euclid_tx` (default: 0):
  * The x position of the euclid on the ROS coordinate system in meters.
- `look_helper/euclid_ty` (default: 0):
  * The y position of the euclid on the ROS coordinate system in meters.
- `look_helper/euclid_tz` (default: 0):
  * The z position of the euclid on the ROS coordinate system in meters.
- `look_helper/euclid_rx` (default: 0):
  * The rotation around the x-axis of the euclid on the ROS coordinate system in degrees.
- `look_helper/euclid_ry` (default: 0):
  * The rotation around the y-axis of the euclid on the ROS coordinate system in degrees.
- `look_helper/euclid_rz` (default: 0):
  * The rotation around the z-axis of the euclid on the ROS coordinate system in degrees.
- `look_helper/webcam_tx` (default: 0):
  * The x position of the webcam on the ROS coordinate system in meters.
- `look_helper/webcam_ty` (default: 0):
  * The y position of the webcam on the ROS coordinate system in meters.
- `look_helper/webcam_tz` (default: 0):
  * The z position of the webcam on the ROS coordinate system in meters.
- `look_helper/webcam_rx` (default: 0):
  * The rotation around the x-axis of the webcam on the ROS coordinate system in degrees.
- `look_helper/webcam_ry` (default: 0):
  * The rotation around the y-axis of the webcam on the ROS coordinate system in degrees.
- `look_helper/webcam_rz` (default: 0):
  * The rotation around the z-axis of the webcam on the ROS coordinate system in degrees.
  
A rotation of 0 on all axes indicates that the camera is facing in the same direction as the CommU.

For more info about the CommU coordinate system, see [CommU.md#coordinate-system](CommU.md#coordinate-system)
For more info about the ROS coordinate system, see [REP 103](http://www.ros.org/reps/rep-0103.html) on the ROS wiki.
  
