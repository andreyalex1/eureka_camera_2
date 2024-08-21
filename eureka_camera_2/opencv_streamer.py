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
        self.pub1 = self.create_publisher(Image, '/micro1/image_raw', 10)
        self.pub2 = self.create_publisher(Image, '/micro2/image_raw', 10)
        timer_period = .1  # seconds
        self.timer = self.create_timer(timer_period, self.spin)
        self.get_logger().info('camera ' + str(name) + " started")
    def __del__(self):
        self.vid1.release() 
        self.vid2.release() 
    def spin(self):
        self.vid1 = cv2.VideoCapture('/dev/micro1', cv2.CAP_V4L2)
        self.vid1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc(*"YUYV"))
        self.vid1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.vid1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.vid1.set(cv2.CAP_PROP_FPS, 10)
        ret, frame = self.vid1.read() 
        print(ret)
        msg = ros2_numpy.msgify(Image, frame, encoding='bgr8') 
        self.pub1.publish(msg)
        self.vid1.release() 
        print("img1 published!")
        self.vid2 = cv2.VideoCapture('/dev/micro2', cv2.CAP_V4L2)
        self.vid2.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc(*"YUYV"))
        self.vid2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.vid2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.vid2.set(cv2.CAP_PROP_FPS, 1)
        ret, frame = self.vid2.read() 
        print(ret)
        msg = ros2_numpy.msgify(Image, frame, encoding='bgr8') 
        self.pub2.publish(msg)
        self.vid2.release()
        print("img2 published!")
        
      



def main(args=None):
    rclpy.init()
    st = opencv_streamer()
    rclpy.spin(st)

    
    st.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()