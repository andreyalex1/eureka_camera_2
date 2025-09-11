from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


#rs_dir = get_package_share_directory('realsense2_camera')

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='pancam',
            namespace='pancam',
            respawn=True,
            respawn_delay=10,
        #    output="screen",
            parameters=["/home/eurekajetson/ros2_ws/src/eureka_camera_2/eureka_camera_2/pancam_parameters.yaml"]
        ),
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='topdowncam',
            namespace='topdowncam',
            respawn=True,
            respawn_delay=10,
      #      output="screen",
            parameters=["/home/eurekajetson/ros2_ws/src/eureka_camera_2/eureka_camera_2/topdowncam_parameters.yaml"]
        ),
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='hazcam',
            namespace='hazcam',
            respawn=True,
            respawn_delay=10,
      #      output="screen",
            parameters=["/home/eurekajetson/ros2_ws/src/eureka_camera_2/eureka_camera_2/hazcam_parameters.yaml"]
        ),
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='armcam',
            namespace='armcam',
            respawn=True,
            respawn_delay=10,
      #      output="screen",
            parameters=["/home/eurekajetson/ros2_ws/src/eureka_camera_2/eureka_camera_2/armcam_parameters.yaml"]
        ),
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='ircam',
            namespace='ircam',
            respawn=True,
            respawn_delay=10,
      #      output="screen",
            parameters=["/home/eurekajetson/ros2_ws/src/eureka_camera_2/eureka_camera_2/ircam_parameters.yaml"]
        ),
    ])