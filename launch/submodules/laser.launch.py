import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    laser_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('sllidar_ros2'), 'launch'),
            '/sllidar_a2m8_launch.py'
            ])
        )

    return LaunchDescription([
        laser_launch,
    ])
