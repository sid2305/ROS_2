import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_1 = self.create_publisher(Float32, 'robot1', 10)
        self.publisher_2 = self.create_publisher(Float32, 'robot2', 10)
        self.publisher_3 = self.create_publisher(Float32, 'robot3', 10)
        self.robo1 = True
        self.robo2 = False
        self.robo3 = False
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 99.115

    def timer_callback(self):
        msg = Float32()
        msg.data = self.i
        if self.robo1:
            self.publisher_1.publish(msg)
            self.robo1 = False
            self.robo2 = True
        elif self.robo2:
            self.publisher_2.publish(msg)
            self.robo2 =False
            self.robo3 = True
        else:
            self.publisher_3.publish(msg)

        self.get_logger().info('Message: "%f"' % msg.data)
        self.i += 0.01


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()