from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    use_sim = {'use_sim_time': 'true'}
    return LaunchDescription([

        Node(package='argus_bot', executable='rsp.launch.py',
             output='screen', parameters=[use_sim]),
        Node(package='gazebo_ros', executable='gzserver',
             arguments=['-s', 'libgazebo_ros_factory.so', '--verbose']),

        Node(package='gazebo_ros', executable='spawn_entity.py',
             arguments=['-topic', 'robot_description', '-entity', 'argus_bot']),

        Node(package='argus_bot', executable='auto_teleop.py',
             output='screen'),
    ])
