# CommU Documentation

This is a concise (and very probably incomplete) guide to using the CommU and Sota robots running the controller software as used in Osaka University's Intelligent Robotics Laboratory. 

## The robots

The two robots used at the Intelligent Robotics Laboratory are Sota and CommU. 

They both run the same controller software and use the same API. The Sota's skin is white with blue accents and is made to look more like a robot, while CommU looks more humanoid with a white-and-beige color. Of the two, Sota is the simpler one. CommU has more degrees of freedom, moving eyes and built in object recognition (**unconfirmed**). This guide is based on the `rev39` version of the codebase in the subversion repository and all information in here was reverse-engineered from the code found on a Sota robot with a Raspberry Pi model 2B as controller. There is also a model of Sota with an Intel Edison, so the details might differ between robots. As for the CommU robot, I have no clue about the internal hardware.

**Note:** I will refer to **both** Sota and CommU robots as **CommU** in the rest of this guide, except for when a distinction between the two is necessary. This is the way it is done in the codebase and will hopefully prevent confusion.

## Overview

The software running on the CommU consists of multiple different applications, all written in C++. 

The main program is called `CommUManager`, which exposes the main API. Another interesting module to gain further information about the API is `SynchyLib`, which controls the CommU's hardware, such as servos, LEDs, the speaker and microphone.

### CommUManager

`CommUManager` ties all of the separate C++ applications together into one API. `CommUManager` is run when the CommU is powered on and uses a YAML file for configuration. 

The location of the configuration file is specified to `CommUManager` with a command line parameter. To find out what configuration file is being used, you'll have to find the script that starts `CommUManager` on boot (e.g. `/etc/rc.local`) and find the file specified with the `-y` flag (e.g. `../../../etc/CommU.yml`). The location of the config file is relative to the location of the `CommUManager` executable (so the example config file would be: `/home/pi/CommU_v3_rev39/etc/CommU.yml`).

The config file specifies parameters for the specific robot, allowing the same software to be run on both CommU and Sota. It also lists gestures and looks, which are a way of making the robot move. These will be discussed in detail later.

#### Config.yml

##### CommUManager

##### LookTable

##### GestureTable



### SynchyLib

`SynchyLib` is the library that is actually controlling the hardware of the robot, and it seems that all other higher-level programs use this to effect the robot. `SynchyLib` provides high-level functions to control the robot including inverse kinematics.


## Gestures

Gestures are an essential part of controlling the CommU. A gesture is specified in a gesture file (typically with a `.s3r` extension) and are read and interpreted by `SynchyLib`.

### Gesture files

A gesture file consist of a number of _gestures_, one on every line. There are a number of different gesture types which indicate different actions.

A general overview of the possible values for a gesture file are specified in the table below.



|     gesture type    | example | explanation|
| ------------------- | ------- | ---------- |
| `p` (lowercase)     |  | With the `p` gesture, we can control multiple joints on the CommU individually. The (lowercase) `p` gesture will send a command to _all_ joints, which means that all other movement going on at the same moment stops, even if the joint is not explicitly specified. |
| `P` (uppercase)     |  | With the `P` gesture, we can control multiple joints on the CommU individually, just as with the (lowercase) `p` gesture. The (uppercase) `P` gesture, however, does not send a command to joints not explicitly specified, so it will allow non-specified joints to keep moving. |
| `a`                 |  | The `a` gesture functionality is exactly the same as that of the (uppercase) `P` gesture, but in the comments it is specified as `Eye` (even though there are no differences in implementation between this and the `P` gesture). |
| `b`                 |  | The `a` gesture functionality is exactly the same as that of the (uppercase) `P` gesture, but in the comments it is specified as `Head` (even though there are no differences in implementation between this and the `P` gesture). |
| `c`                 |  | The `a` gesture functionality is exactly the same as that of the (uppercase) `P` gesture, but in the comments it is specified as `Right Arm` (even though there are no differences in implementation between this and the `P` gesture). |
| `d`                 |  | The `a` gesture functionality is exactly the same as that of the (uppercase) `P` gesture, but in the comments it is specified as `Left arm` (even though there are no differences in implementation between this and the `P` gesture). |
| `e`                 |  | The `a` gesture functionality is exactly the same as that of the (uppercase) `P` gesture, but in the comments it is specified as `Waist` (even though there are no differences in implementation between this and the `P` gesture). |
| `f`                 |  | The `a` gesture functionality is exactly the same as that of the (uppercase) `P` gesture, but in the comments it is specified as `Wheel` (even though there are no differences in implementation between this and the `P` gesture). |
| `m`                 |  | The `m` gesture functionality is exactly the same as that of the (uppercase) `P` gesture, but in the comments it is specified as `Mouth` (even though there are no differences in implementation between this and the `P` gesture). |
| `g`                 |  | The `g` gesture allows us to specify another gesture file that will be loaded and executed at the specified time. |
| `u` (unimplemented) |  | The `u` gesture seems to provide some sort of utter support, but is not implemented. |
| `w` (lowercase)     |  | The `w` gesture specifies an object id for the CommU to look at. It is not clear where this object id should come from, nor does it ever seem to be used. Object recognition is definitely not implemented on the Sota robot, but it might be on the CommU. |
| `W` (uppercase)     |  | The `W` gesture specifies a location for the CommU to look at, using x y and z coordinates. This feature, with more functions is also provided under `/look` in the API |
| `l`                 |  | The `l` gesture seems to provide LED control, but doesn`t seem to work on my Sota. |
| `t` (_required_)    |  | The `t` 'gesture' specifies after how many seconds this should end. When the `t` gesture is reached, the gesture will be terminated. This is **required** for every gesture.



The first two parameters for any gesture are a float indicating the time at which the gesture should be executed relative to the start of the gesture and a character indicating the gesture type (case matters).

| gesture type |  parameter  | explanation |
| ------------ | ----------- | ----------- |
| `P`          |             |




## TCP API


