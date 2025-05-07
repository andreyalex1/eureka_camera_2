from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    json_config_path = os.path.join(
        get_package_share_directory('eureka_camera_2'),
        'launch',
        'real.json'
    )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('realsense2_camera'),
                    'launch',
                    'rs_launch.py'
                )
            ),
            launch_arguments={
                # Основные настройки
                'device_type': 'd435i',  
                'enable_depth': 'true',  
                'enable_color': 'true',  
                'align_depth.enable': 'true',  
                'enable_sync': 'true',
                'enable_infra1': 'false',  
                'enable_infra2': 'false',
                'enable_pointcloud': 'true',  
                'pointcloud.allow_no_texture_points': 'true',  
                'spatial_filter.enable': 'true',  
                'spatial_filter.filter_magnitude': '1.0',
                'spatial_filter.filter_smooth_alpha': '0.54',
                'spatial_filter.filter_smooth_delta': '7.0',
                'hole_filling_filter.enable': 'true',  
                'temporal_filter.enable': 'false',  
                'disparity_filter.enable': 'false',  
                'decimation_filter.enable': 'false',                  
                'enable_gyro': 'false',
                'enable_accel': 'false',                
                'tf_publish_rate': '10.0',  
                'depth_fps': '15',  
                'color_fps': '15', 
                'json_file_path': 'src/eureka_camera_2/launch/real.json',                
                'initial_reset': 'false',  
            }.items()
        )
    ])