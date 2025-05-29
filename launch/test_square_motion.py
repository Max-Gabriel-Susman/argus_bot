import rclpy
import pytest
import launch_testing
from launch_testing.asserts import assertAlmostEqual


@pytest.mark.rostest
def generate_test_description():
    from launch_ros.actions import Node
    from launch import LaunchDescription
    ld = LaunchDescription()
    ld.add_action(Node(package='argus_bot', executable='test_square_motion.launch.py'))
    return ld, {}


class SquareMotionTest(launch_testing.TestCase):

    def test_final_pose(self, proc_output):
        rclpy.init()
        node = rclpy.create_node('pose_listener')
        pose = None

        def cb(msg):
            nonlocal pose
            pose = msg.pose.pose

        end = node.get_clock().now() + rclpy.duration.Duration(seconds=45)
        while rclpy.ok() and node.get_clock().now() < end and pose is None:
            rclpy.spin_once(node, timeout_sec=0.1)

        assert pose is not None, "No odom received"
        assertAlmostEqual(pose.position.x, 0.0, 0.2)
        assertAlmostEqual(pose.position.y, 0.0, 0.2)
        rclpy.shutdown()
