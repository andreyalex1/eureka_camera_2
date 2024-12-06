from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


rs_dir = get_package_share_directory('realsense2_camera')

def generate_launch_description():
    return LaunchDescription([
       IncludeLaunchDescription(
            launch_description_source = PythonLaunchDescriptionSource(rs_dir + '/launch/rs_launch.py'),
            launch_arguments={
                            'device_type' : 'd435',
                            'pointcloud.enable' : 'true', 
                            'pointcloud.allow_no_texture_points' : 'true',
                            'unite_imu_method' :  '2', 
                            'enable_gyro': 'true', 
                            'enable_accel': 'true',
                            'tf_publish_rate': '10',
                            'hdr_merge.enable' : 'true',
                            # 'align_depth.enable':'true'
                            'decimation_filter.enable' : 'false',#maybe
                            'spatial_filter.enable' : 'true',  
                            'spatial_filter.filter_magnitude' : '1.0',
                            'spatial_filter.filter_smooth_alpha': '0.54',
                            'spatial_filter.filter_smooth_delta': '7.0', 
                            'temporal_filter.enable' :   'false',
                            'temporal_filter.filter_smooth_alpha': '1.0',
                            'temporal_filter.filter_smooth_delta': '100.0',
                            'disparity_filter.enable' :  'false',
                            'hole_filling_filter.enable' : 'true',
                            'hdr_merge.enable' : 'true',
                            'disparity_to_depth.enable': 'true',
                            'json_file_path': 'src/eureka_camera_2/launch/real.json',

          #                  'initial_reset' : 'true'
                            }.items()
        ),
   #     Node(
   #         package='usb_cam',
   #         executable='usb_cam_node_exe',
   #         name='hazcam',
   #         namespace='hazcam',
   #         output="screen",
   #         parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/hazcam_parameters.yaml"]
  #      ),
      #  Node(
     #       package='usb_cam',
    #        executable='usb_cam_node_exe',
     #       name='pancam',
     #       namespace='pancam',
        #    output="screen",
     #       parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/pancam_parameters.yaml"]
     #   ),
     #   Node(
      #      package='usb_cam',
     #       executable='usb_cam_node_exe',
      #      name='topdowncam',
      #      namespace='topdowncam',
       #     output="screen",
       #     parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/topdowncam_parameters.yaml"]
      #  ),
 #       Node(
 #           package='usb_cam',
 #           executable='usb_cam_node_exe',
 #           name='armcam',
 #           namespace='armcam',
 #           output="screen",
 #           parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/armcam_parameters.yaml"]
 #       ),
 #       Node(
 #           package='eureka_camera_2',
 #           executable='opencv_streamer',
 #           name='opencv_streamer',
 #           shell=True,
 #       ),
 #       Node(
 #           package='usb_cam',
 #           executable='usb_cam_node_exe',
 #           name='armncam',
  #          namespace='armcam',
  #          parameters=["/home/eurekanuc/ros2_ws/src/eureka_camera_2/eureka_camera_2/armcam_parameters.yaml"]
  #     ),
        
    ])
