# Python3 ROS2 Node to control the camera shutter
# Subscribing to: '/v4l/camera/image_raw/compressed'
# and trigger signal subscribed from '/trigger'

import rclpy
import threading
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Empty
from std_msgs.msg import String
from cv_bridge import CvBridge
import time

import cv2

class CameraShutter(Node):
    def __init__(self):
        super().__init__('camera_shutter')
        empty_subscription = self.create_subscription(Empty, '/shutter', self.trigger_callback, 10)
        image_subscription = self.create_subscription(CompressedImage, '/v4l/camera/image_raw/compressed', self.image_callback, 10)
        # Mutex
        self.lock = threading.Lock()
        self.image = None
        # CV Bridge
        self.cv_bridge = CvBridge()

    def trigger_callback(self, msg):
        """
        If Receive signal - Write the self.image with cv2 imwrite

        Args:
            msg (_type_): _description_
        """
        self.get_logger().info('Trigger signal received')
        with self.lock:
            if self.image is not None:
                # Filename Generate from timestamp
                filename = 'image-{}.jpg'.format(time.time())
                cv2.imwrite(filename, self.image)
                self.get_logger().info('Image saved')

    def image_callback(self, msg):
        self.get_logger().info('Image received')
        with self.lock:
            self.image = self.cv_bridge.compressed_imgmsg_to_cv2(msg)

def main():
    rclpy.init()
    cam_shutter = CameraShutter()

    rclpy.spin(cam_shutter)
    rclpy.shutdown()

if __name__ == '__main__':
    main()