# ros-commu
The catkin workspace folder for my commu dialogue project at Osaka University's Intelligent Robotics Laboratory

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
roslaunch dialogue dialogue.launch commu-ip:=192.168.1.1 commu-port:=6019 camera-path:=/dev/video0
```

The launch file accepts 3 arguments:
- `commu-ip` (required):
  * The IP address of the CommU robot.
- `commu-port` (default: 6001): 
  * The port of the CommU manager program on the CommU.
- `camera-path` (default: /dev/fisheye-camera):
  * The path to the video device to use as input. The video device has to be connected to the GPU-pc. It is also possible to use another camera, by remapping the raw output topic of the camera to `/cv_camera/image_raw`.
- `euclid` (default: EUCLID_70FD):  
  * The hostname of the Intel Euclid Development Kit.