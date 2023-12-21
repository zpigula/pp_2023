#!/bin/bash

set -e

source "/opt/ros/$ROS_DISTRO/setup.bash"
cd
cd dev_ws
colcon build
source "/home/zp/dev_ws/install/setup.bash"

echo "Provided arguments: $@"

exec $@