# zbot package

This package contains zbot URDF file and a launch script to run it in Gazebo & rviz2. 
(ROS 2 docker container: r2_zbot_dev)

## How To Run
0. Start docker container and open bash terminal

```
sudo docker container start r2_zbot_dev
docker exec -it r2_zbot_dev bash

```
1. Build the package with colcon:

```
colcon build --symlink-install
source install/setup.bash

```

2. Launch Gazebo simulation: 

`ros2 launch zbot rsp_sim.launch_zbot.py world:=./src/zbot/worlds/turtlebot3_house.world`

3. Launch RViz with `rviz2`

- Set your fixed frame to `odom`
- Add a `RobotModel` display, with the topic set to `/robot_description`
- Add a `TF` display with names enabled.

4. Launch teleop:

`run teleop_twist_keyboard teleop_twist_keyboard`