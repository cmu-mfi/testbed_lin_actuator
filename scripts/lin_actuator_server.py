from testbed_lin_actuator.LinearActuator import LinearActuator
import numpy as np
import time

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Bool, Empty, Int16
import argparse

class LinearActuatorServer:
    def __init__(self, port):
        self.la = LinearActuator(port)
        self.pub = rospy.Publisher('/linear_actuator_joint_states', JointState, queue_size=10)
        self.reset_sub = rospy.Subscriber('/reset', Empty, self.reset_callback)
        self.stop_sub = rospy.Subscriber('/stop', Bool, self.stop_callback)
        self.toggle_sub = rospy.Subscriber('/toggle', Int16, self.toggle_callback)
        self.joint_names = ['lin_actuator_1', 'lin_actuator_2']
        self.joint_states = np.zeros(2)
        self.minimum_joint_positions = np.array([0.003, 0.0017])
        self.maximum_joint_positions = np.array([0.09, 0.092])
        self.la.reset()
        
    def reset_callback(self, msg):
        self.la.move_joint_position(self.minimum_joint_positions, [1.0])

    def stop_callback(self, msg):
        if msg.data:
            self.la.stop()
        else:
            self.la.start()

    def toggle_callback(self, msg):
        self.joint_states[msg.data-1] = (self.joint_states[msg.data-1] + 1) % 2

        desired_joint_positions = np.zeros(2)
        desired_joint_positions[self.joint_states == 0] = self.minimum_joint_positions[self.joint_states==0]
        desired_joint_positions[self.joint_states == 1] = self.maximum_joint_positions[self.joint_states==1]
        self.la.move_joint_position(desired_joint_positions, [1.0])

    def publish_joint_state_msg(self):
        joint_state_msg = JointState()
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.name = self.joint_names
        current_joint_positions, current_joint_velocities = self.la.get_joint_positions_and_velocities()
        joint_state_msg.position = current_joint_positions
        joint_state_msg.velocity = current_joint_velocities

        self.pub.publish(joint_state_msg)
        

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--port', '-p', default='/dev/ttyACM0')
    #args = parser.parse_args()

    rospy.init_node('lin_actuator_server', anonymous=True)
    rate = rospy.Rate(100) # 10hz

    las = LinearActuatorServer('/dev/ttyACM0')

    while not rospy.is_shutdown():
        las.publish_joint_state_msg()
        rate.sleep()
