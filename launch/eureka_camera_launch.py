from launch import LaunchDescription
from launch_ros.actions import Node
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='hazcam',
            namespace='hazcam',
            parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/hazcam_parameters.yaml"]
        ),
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='pancam',
            namespace='pancam',
            parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/pancam_parameters.yaml"]
        ),
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='topdowncam',
            namespace='topdowncam',
            parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/topdowncam_parameters.yaml"]
        ),
        Node(
            package='web_video_server',
            executable='web_video_server',
            name='web_video_server',
        ),
    ])