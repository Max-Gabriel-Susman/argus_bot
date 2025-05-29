import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class AutoTeleop(Node):
    def __init__(self):
        super().__init__('auto_teleop')
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.step)   # 10 Hz
        self.start_time = self.get_clock().now().seconds_nanoseconds()[0]

    def step(self):
        t = self.get_clock().now().seconds_nanoseconds()[0] - self.start_time
        msg = Twist()

        phase = int(t / 5)
        if phase % 2 == 0:
            msg.linear.x = 0.4
        else:
            msg.angular.z = math.pi/10

        if phase >= 8:
            rclpy.shutdown()
            return

        self.pub.publish(msg)


def main():
    rclpy.init()
    rclpy.spin(AutoTeleop())


if __name__ == '__main__':
    main()
