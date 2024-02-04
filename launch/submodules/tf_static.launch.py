from launch import LaunchDescription
from launch_ros.actions import Node

import numpy as np

def generate_launch_description():
    laser_tf_static_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments = ['--x', '0.1', '--y', '0', '--z', '0.1', '--yaw', str(np.pi), '--pitch', '0', '--roll', '0', '--frame-id', 'base_link', '--child-frame-id', 'laser']
    )

    return LaunchDescription([
        laser_tf_static_node,
    ])
