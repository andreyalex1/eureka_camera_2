from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


rs_dir = get_package_share_directory('realsense2_camera')

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='hazcam',
            namespace='hazcam',
        #    output="screen",
            parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/hazcam_parameters.yaml"]
        ), 
        
    ])