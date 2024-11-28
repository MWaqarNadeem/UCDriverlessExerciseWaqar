import rclpy
from rclpy.node import Node
from sysmonitor_interfaces.msg import Sysmon

from std_msgs.msg import Float64

class SystemPublisher(Node):

    def __init__(self):
        super().__init__('system_publisher')
        self.publisher_ = self.create_publisher(Float64, '/test', 10)
        self.subscription = self.create_subscription(
            Sysmon,
            '/system_info',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        value_to_publish = Float64()
        value_to_publish.data = msg.cpu_usage  # we will use 'cpu_usage` from Sysmon message
        self.publisher_.publish(value_to_publish)
        self.get_logger().info(f'Publishing: "{value_to_publish.data}" on /test')

def main(args=None):
    rclpy.init(args=args)
    system_publisher = SystemPublisher()
    rclpy.spin(system_publisher)
    system_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()