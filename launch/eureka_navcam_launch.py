from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='camera',                     
            namespace='camera',                 
            parameters=[{
                'device_type': 'd435i',
                'enable_color': True,          
                'enable_depth': True,           
                'align_depth.enable': True,     
                'pointcloud.enable': True,      
                'pointcloud.allow_no_texture_points': True,
                
                'color_width': 640,
                'color_height': 480,
                'depth_width': 640,
                'depth_height': 480,
                'color_fps': 30,
                'depth_fps': 30,
                
                'enable_gyro': False,
                'enable_accel': False,
                'hdr_merge.enable': False,
                'spatial_filter.enable': False,
                'temporal_filter.enable': False,
                'hole_filling_filter.enable': False,
                'json_file_path': 'src/eureka_camera_2/launch/real.json',
            }]
        )
    ])