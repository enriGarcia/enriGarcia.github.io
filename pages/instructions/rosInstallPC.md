---
layout: page
title: Instalación de ROS
description: Instalación de ROS Noetic en Ubuntu 20.04
---
> Este tutorial es para usuarios que tengan instalado el módulo de Sympy. Si aún no lo ha instalado de click aquí.

# Índice
- [1. Funciones](#1.-funciones)


# 1. Funciones
[Volver al Índice](#índice)

# Instalación de ROS
## Instalación de ROS Noetic en Ubuntu 20.04

1. Primero, es importante crear un entorno virtual llamado `ros1` para aislar la instalación. Esto es importante para que en el mismo equipo ROS1 y ROS2 puedan ser utilizados.

```console
$ sudo apt install python3-pip
$ sudo pip install virtualenv virtualenvwrapper
$ sudo rm -rf ~/.cache/pip get-pip.py
$ echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
$ echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
$ echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
$ source ~/.bashrc
$ mkvirtualenv ros1 -p python3
$ workon ros1
```

2. Después se debe actualizar la lista de fuentes de datos `sources.list`:
```console
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

3. También se actualizan las llaves:
```console
$ sudo apt install curl
$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

4. Se actualiza el índice de paquetes de Debian:
```console
$ sudo apt update
```
5. Posteriormente se instala la versión `ROS Desktop-Full`:
```console
$ sudo apt install ros-noetic-desktop-full
```

You must source this script in every bash terminal you use ROS in.
```console
$ echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

Up to now you have installed what you need to run the core ROS packages. To create and manage your own ROS workspaces, there are various tools and requirements that are distributed separately. For example, rosinstall is a frequently used command-line tool that enables you to easily download many source trees for ROS packages with one command. To install this tool and other dependencies for building ROS packages, run:
```console
$ workon ros1
$ sudo apt install python3-roslaunch python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential 
```

Type `roscore` to test the correct installation
```console
$ roscore
```
To exit `roscore` type `Ctrl + C`

Source ROS Noetic
```console
$ source /opt/ros/noetic/setup.bash
```

## Create a ROS Workspace
Finishing the installation you need to setup your enviroment
Let's create and build a catkin workspace:
```console
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
```

Source `devel`
```console
$ source devel/setup.bash
```

To make sure your workspace is properly overlayed by the setup script, make sure `ROS_PACKAGE_PATH` environment variable includes the directory you're in.

```console
$ echo $ROS_PACKAGE_PATH
```
Must print `/home/enri/catkin_ws/src:/opt/ros/noetic/share`

Test code from Anis Koubaa by cloning his repository

```console
$ cd ~/catkin_ws/src/
$ git clone -b ros-noetic https://github.com/aniskoubaa/ros_essentials_cpp.git
$ cd ros_essentials_cpp
$ cd ~/catkin_ws/
$ catkin_make
```
We can close the terminal window

### Testing your installation with cpp nodes
This must be run everytime we close a terminal window:

On a new terminal run `roscore`
```console
$ workon ros1
$ cd ~/catkin_ws/
$ source devel/setup.bash
$ echo $ROS_PACKAGE_PATH
$ cd ~
$ roscore
```

Testing an example of Talker and Listener on other Terminal

On a new terminal run `ros_essentials_cpp talker_node`
```console
$ workon ros1
$ cd ~/catkin_ws/
$ source devel/setup.bash
$ cd ~
$ rosrun ros_essentials_cpp talker_node
```
On another terminal run `ros_essentials_cpp listener_node`
```console
$ workon ros1
$ cd ~/catkin_ws/
$ source devel/setup.bash
$ cd ~
$ rosrun ros_essentials_cpp listener_node
```

To exit `talker_node` and `listener_node` type `Ctrl + C` on each terminal.

Close all terminals.
### Testing your installation with python nodes
Run `roscore` on a new terminal 
```console
$ workon ros1
$ pip install pyyaml
$ pip install rospkg
$ cd ~/catkin_ws/
$ source devel/setup.bash
$ cd ~
$ roscore
```
Open a new terminal, then run `rosrun ros_essentials_cpp talker.py`

```console
$ workon ros1
$ cd ~/catkin_ws/
$ source devel/setup.bash
$ cd ~
$ rosrun ros_essentials_cpp talker.py
```
Open a new terminal, then run `rosrun ros_essentials_cpp listener.py`

```console
$ workon ros1
$ cd ~/catkin_ws/
$ source devel/setup.bash
$ cd ~
$ rosrun ros_essentials_cpp listener.py
```
To exit `talker` and `listener` type `Ctrl + C` on each terminal.

Close all terminals.

## Briefing
ROS is installed in `/opt/ros/noetic`. In this directory we can find the *ROS workspace* or working area. Any workspace would have special files like `setup.bash`, `setup.sh` and `setup.zsh` for different types of shells, and these must be executed to enable the workspace. In bash we need to source `setup.bash` in order to enable ROS workspace. We can do this manually everytime we need work with ROS in a new terminal, but it is better to edit the `.bashrc` which is a file that automatically is executed when a new terminal is open. So `.bashrc` contains several script lines that are executed whenever we open a new terminal.

If the line `source /opt/ros/noetic/setup.bash` is commented or deleted we will have errors when running `roscore` or `roscd`. Error is going to persist even when we uncommented the line. So terminal window must be closed and replaced with a new one. If we run `roscd` it will point to `/opt/ros/noetic` no matter the virtual environment, which is the default ROS workspace.

It is not convenient to work in main ROS workspace so it is common to create our own workspace with custom ROS projects, custom `roscore` and `roscd`. That's the reason we created `catkin_ws`, however it can be any other workspace if we follow these instructions:
```console
$ cd ~
$ mkdir -p ~/custom_ws/src
```

And compile the workspace using `catkin_make` remebering to use the virtual enviroment ros1:
```console
$ workon ros1
$ cd ~/custom_ws
$ catkin_make
```
However if we run `roscd` it will point to `/opt/ros/noetic` again so we need to source the new workspace's `setup.bash`. This can be done automatically everytime we open a new terminal if we edit `.bashrc`. In these case, for `catkin_ws` we add the following line to `.bashrc`: `source /home/enri/catkin_ws/devel/setup.bash`. Remebering to close all other terminals and open a new one if we type again `roscd` it will point to `~/catkin_ws/devel`

## Creating ROS Projects
A ROS project is actually called a *package* and a package is defined inside a workspace. If we go to the catkin workspace `catkin_ws` there will be three directories:

- `build`: contains the compiled files
- `devel`: development
- `src`: source files

Packages must be created within `src` directory using `catkin_create_pkg package_name dependencies`. For example if we want to create `ros_basics_tutorials`:
```console
$ workon ros1
$ cd ~/catkin_ws/src
$ catkin_create_pkg ros_basics_tutorials std_msgs rospy roscpp
```

Dependencies in `ros_basics_tutorials` are `std_msgs` for standard messages, `rospy` for python development and `roscpp` for cpp development. These are usually a must dependencies when creating a new package. Then, we need to compile again the workspace.
```console
$ workon ros1
$ cd ~/catkin_ws/
$ catkin_make
```
There will be a new directory on `~/catkin_ws/src` named `ros_basics_tutorials` and inside `~/catkin_ws/src/ros_basics_tutorials` it will be a `/src` directory where we will be adding the source code of our project and a `/include` folder where we can add libraries.



<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->

<!--
To increase the size of the title, use fewer # in front of the paper title.
To decrease the size of the title, use more #. 
To remove the italics, remove the * before and after the description
To remove the underline from the title, remove the <u> tags (<u> and </u>)
-->
