#!/usr/bin/env python3

#Developed by Andrei Smirnov. 2024
#MSU Rover Team. Voltbro. NIIMech 
import numpy as np
import rclpy
from rclpy.node import Node
import ros2_numpy

from sensor_msgs.msg import Image
# import the opencv library 
import cv2 

#print(cv2.getBuildInformation())
  
class opencv_streamer(Node):
    def __init__(self, name='cam1'):
        super().__init__('opncv_streamer')
        self.name = name
        self.pub = self.create_publisher(Image, 'image_raw', 10)
        self.vid = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)
        self.vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc(*"MJPG"))
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.vid.set(cv2.CAP_PROP_FPS, 30)
        width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

        print(width,height)
        timer_period = 0.003  # seconds
        self.timer = self.create_timer(timer_period, self.spin)
        self.get_logger().info('camera ' + str(name) + " started")
    def __del__(self):
        self.vid.release() 
    def spin(self):
        ret, frame = self.vid.read() 
        msg = ros2_numpy.msgify(Image, frame, encoding='bgr8') 
        print(1)
        self.pub.publish(msg)
      



def main(args=None):
    rclpy.init()
    st = opencv_streamer()
    rclpy.spin(st)

    
    st.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()