# generic launch actions
from launch.actions import IncludeLaunchDescription
from launch.actions import SetEnvironmentVariable

# ROS specific launch actions
from launch_ros.actions import Node

import os
import xacro

from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription


def generate_launch_description():

    # Specify the name of the package and path to xacro file within the package
    pkg_name = 'zbot'
    file_subpath = 'description/zbot.urdf.xacro'

    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # Set GAZEBO_MODEL_PATH - will be used by gazebo to find model/mesh files
    pkg_install_path = get_package_share_directory(pkg_name)
    if 'GAZEBO_MODEL_PATH' in os.environ:
        model_path =  os.environ['GAZEBO_MODEL_PATH'] + ':' + pkg_install_path
    else:
        model_path =  pkg_install_path + '/models'


    print("GAZEBO MODEL PATH==" + model_path)

    # Configure the node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw,
        'use_sim_time': True}] # add other parameters here if required
    )

    gazebo_params_file = os.path.join(get_package_share_directory(pkg_name),'config','gazebo_params.yaml')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
            launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
        )

    spawn_robot_into_gazebo = Node(
        package='gazebo_ros', executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'zbot'], 
        output='screen')
    
    diff_drive_spawner = Node(
        package="controller_manager",
        executable='spawner',
        arguments=["diff_cont"])

    joint_broad_spawner = Node(
            package="controller_manager",
            executable='spawner',
            arguments=["joint_broad"])



    # Run the node
    return LaunchDescription([
        SetEnvironmentVariable(name='GAZEBO_MODEL_PATH', value=model_path),
        gazebo,
        node_robot_state_publisher,
        spawn_robot_into_gazebo,

        diff_drive_spawner,
        joint_broad_spawner
    ])




