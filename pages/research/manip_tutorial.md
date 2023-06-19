---
layout: page
title: URDF Manipulator Tutorial
description:
---
# Custom URDF manipulators tutorial

## Workspace

A workspace named `ws_manipulators` is created.

```bash
$ mkdir -p ~/ROS/ws_manipulators/src
$ cd ~/ROS/ws_manipulators/src/
$ catkin_init_workspace
$ catkin_create_pkg manip1 std_msgs rospy
$ cd ~/ROS/ws_manipulators/
$ catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
```

## URDF Model
```bash
$ mkdir -p ~/ROS/ws_manipulators/src/manip1/urdf
$ mkdir -p ~/ROS/ws_manipulators/src/manip1/rviz
$ cd ~/ROS/ws_manipulators/src/manip1/urdf/
```
Inside this folder create the file `manip1.xacro` with the following contents:

```xml
<?xml version="1.0"?>

<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="manip1">

   <xacro:property name="joint_min_lim" value="${-pi/2}"/>
   <xacro:property name="joint_max_lim" value="${pi/2}"/>
   <xacro:property name="width" value="0.080"/>
   <xacro:property name="L1" value="0.500"/>
   <xacro:property name="L2" value="0.300"/>
   <xacro:property name="L3" value="0.250"/>
   <xacro:property name="L4" value="0.050"/>
   <xacro:property name="m4" value="0.300"/>

   <!--Cylinder--> 
   <xacro:macro name="default_cylinder" params="length">
       <origin xyz="0.0 0.0 ${length/2}" rpy="0.0 0.0 0.0"/>
       <geometry>
           <cylinder radius="${width/2}" length="${length}"/>
       </geometry>
   </xacro:macro>

   <!--Cube--> 
   <xacro:macro name="default_cube" params="length">
       <origin xyz="0.0 0.0 ${length/2}" rpy="0.0 0.0 0.0"/>
       <geometry>
           <box size="${length} ${length} ${length}"/>
       </geometry>
   </xacro:macro>

   <!--Inertial cuboid--> 
    <xacro:macro name="inertial_cuboid" params="m lx ly lz">
        <origin xyz="0.0 0.0 0.0" rpy="0.0 0.0 0.0"/>
        <mass value="${m}"/>
        <inertia 
            ixx="${(1/12)*m*(ly**2 + lz**2)}"
            ixy="0.0" 
            ixz="0.0" 
            iyy="${(1/12)*m*(lz**2 + lx**2)}"
            iyz="0.0" 
            izz="${(1/12)*m*(lx**2 + ly**2)}" />
    </xacro:macro>

   <!--Materials--> 
   <material name="white">
       <color rgba="0.8 0.8 0.8 1.0"/>
   </material>
   <material name="red">
       <color rgba="0.8 0.0 0.0 0.5"/>
   </material>

   <!--World--> 
   <link name="world">
   </link>

   <!--Base--> 
   <link name="base_link">
    <inertial>
        <xacro:inertial_cuboid m="5.000" lx="0.400" ly="0.400" lz="0.010"/>
    </inertial>
    <visual> 
        <origin xyz="0.0 0.0 0.0" rpy="0.0 0.0 0.0"/>
        <geometry>
            <box size="0.400 0.400 0.010"/>
        </geometry>
        <material name="white">
        </material>
    </visual>
   </link>
   <joint name="base_joint" type="fixed">
        <origin xyz="0.0 0.0 0.0" rpy="0.0 0.0 0.0"/>
        <parent link="world"/>
        <child link="base_link"/>
   </joint>

   <!--Link_1--> 
   <link name="link_1">
    <inertial>
        <origin xyz="0.0 0.0 0.0" rpy="0.0 0.0 0.0"/>
        <mass value="0.0"/>
        <inertia ixx="0.0" ixy="0.0" ixz="0.0" iyy="0.0" iyz="0.0" izz="0.0"/>
    </inertial>
    <visual>
        <xacro:default_cylinder length="${L1}"/>
        <material name="red">
        </material>
    </visual>
    <collision>
        <xacro:default_cylinder length="${L1}"/>
    </collision>
   </link>
   <joint name="joint_1" type="revolute">
        <origin xyz="0.0 0.0 0.0" rpy="0.0 0.0 0.0"/>
        <parent link="base_link"/>
        <child link="link_1"/>
        <axis xyz="0.0 0.0 1.0"/>
        <limit lower="${joint_min_lim}" upper="${joint_max_lim}" effort="0.0" velocity="0.0"/>
   </joint>

   <!--Link_2--> 
   <link name="link_2">
    <inertial>
        <origin xyz="0.0 0.0 0.0" rpy="0.0 0.0 0.0"/>
        <mass value="0.0"/>
        <inertia ixx="0.0" ixy="0.0" ixz="0.0" iyy="0.0" iyz="0.0" izz="0.0"/>
    </inertial>
    <visual>
        <xacro:default_cylinder length="${L2}"/>
        <material name="white">
        </material>
    </visual>
    <collision>
        <xacro:default_cylinder length="${L2}"/>
    </collision>
   </link>
   <joint name="joint_2" type="revolute">
        <origin xyz="0.0 ${-width} ${L1}" rpy="0.0 ${pi/2} 0.0"/>
        <parent link="link_1"/>
        <child link="link_2"/>
        <axis xyz="0.0 1.0 0.0"/>
        <limit lower="${joint_min_lim}" upper="${joint_max_lim}" effort="0.0" velocity="0.0"/>
   </joint>
   
   <!--Link_3--> 
   <link name="link_3">
    <inertial>
        <origin xyz="0.0 0.0 0.0" rpy="0.0 0.0 0.0"/>
        <mass value="0.0"/>
        <inertia ixx="0.0" ixy="0.0" ixz="0.0" iyy="0.0" iyz="0.0" izz="0.0"/>
    </inertial>
    <visual>
        <xacro:default_cylinder length="${L3}"/>
        <material name="red">
        </material>
    </visual>
    <collision>
        <xacro:default_cylinder length="${L3}"/>
    </collision>
   </link>
   <joint name="joint_3" type="revolute">
        <origin xyz="0.0 ${width} ${L2}" rpy="0.0 0.0 0.0"/>
        <parent link="link_2"/>
        <child link="link_3"/>
        <axis xyz="0.0 1.0 0.0"/>
        <limit lower="${joint_min_lim}" upper="${joint_max_lim}" effort="0.0" velocity="0.0"/>
   </joint>

   <!--Link_4--> 
   <link name="link_4">
    <inertial>
        <xacro:inertial_cuboid m="${m4}" lx="${L4}" ly="${L4}" lz="${L4}"/>
    </inertial>
    <visual>
        <xacro:default_cube length="${L4}"/>
        <material name="white">
        </material>
    </visual>
    <collision>
        <xacro:default_cube length="${L4}"/>
    </collision>
   </link>
   <joint name="joint_4" type="revolute">
        <origin xyz="0.0 0.0 ${L3}" rpy="0.0 0.0 0.0"/>
        <parent link="link_3"/>
        <child link="link_4"/>
        <axis xyz="0.0 0.0 1.0"/>
        <limit lower="${joint_min_lim}" upper="${joint_max_lim}" effort="0.0" velocity="0.0"/>
   </joint>

</robot>
```
Test the file `manip1.xacro` running the following command:

```bash
$ cd ~/ROS/ws_manipulators/src/manip1/urdf
$ roslaunch urdf_tutorial display.launch model:=manip1.xacro
```
RVIZ will open showing the robot and the joint controller.
![URDF Model on RVIZ]({{BASE_PATH}}/assets/figures/rviz_manip1.png)

## RVIZ launch file

Create the directory `launch` on `~/ROS/ws_manipulators/src/manip1`:
```bash
$ mkdir -p ~/ROS/ws_manipulators/src/manip1/launch
```
Add the file `manip1_rviz.launch` on `launch` directory with the following contents:

```xml
<launch>

  <arg name="model" default="$(find manip1)/urdf/manip1.xacro"/>
  <arg name="gui" default="true" />
  <arg name="rvizconfig" default="$(find manip1)/rviz/urdf.rviz"/>

  <param name="robot_description" command="$(find xacro)/xacro $(arg model)"/>
  <param name="use_gui" value="$(arg gui)"/>

  <node name="joint_state_publisher_gui" pkg="joint_state_publisher_gui" type="joint_state_publisher_gui"/>
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher"/>
  <node name="rviz" pkg="rviz" type="rviz" args="-d $(arg rvizconfig)" required="true"/>

</launch>
```

Add the file `urdf.rviz` on `~/ROS/ws_manipulators/src/manip1/rviz` with the following contents:

```json
Panels:
  - Class: rviz/Displays
    Name: Displays
  - Class: rviz/Views
    Name: Views
Visualization Manager:
  Displays:
    - Class: rviz/Grid
      Name: Grid
      Value: true
    - Alpha: 0.8
      Class: rviz/RobotModel
      Enabled: true
      Name: RobotModel
      Robot Description: robot_description
      Value: true
    - Class: rviz/TF
      Name: TF
      Value: true
      Marker Scale: 0.4
  Global Options:
    Fixed Frame: base_link
    Frame Rate: 30
  Name: root
  Tools:
    - Class: rviz/MoveCamera
  Value: true
  Views:
    Current:
      Class: rviz/Orbit
      Distance: 1.7
      Name: Current View
      Pitch: 0.33
      Value: Orbit (rviz)
      Yaw: 5.5
Window Geometry:
  Height: 800
  Width: 1200
```

Add the following line to `.bashrc`

```bash
source ~/ROS/ws_manipulators/devel/setup.bash
```
Remember to comment any other ROS workspaces, as in my case:

```bash
source /opt/ros/noetic/setup.bash
# Commented because not active ROS workspace
# source ~/ROS/ws_moveit/devel/setup.bash
source ~/ROS/ws_manipulators/devel/setup.bash
```
Close the current terminal and open a new one. If you type `$ roscd` it will point to `~/ROS/ws_manipulators/devel$`

Run to launch RVIZ with robot model and joint publisher GUI.

```bash
$ roslaunch manip1 manip1_rviz.launch
```
![Custom RVIZ launcher]({{BASE_PATH}}/assets/figures/rviz_manip2.png)
