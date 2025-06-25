import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node

class IRImageProcessor(Node):
    def __init__(self):
        super().__init__('ir_image_processor')
        self.subscription = self.create_subscription(
            Image,
            '/camera/camera/infra1/image_rect_raw',
            self.listener_callback,
            10)
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')

        # Применение шумоподавления
        denoised = cv2.fastNlMeansDenoising(cv_image, None, 10, 7, 21)

        # Улучшение контраста с помощью CLAHE
        gray_image = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        cl1 = clahe.apply(gray_image)

        # Увеличение резкости
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        sharpened = cv2.filter2D(cl1, -1, kernel)

        # Отображение изображения
        cv2.imshow("Denoised and Enhanced Image", sharpened)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    ir_image_processor = IRImageProcessor()
    rclpy.spin(ir_image_processor)
    ir_image_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()