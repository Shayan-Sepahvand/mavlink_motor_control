#!/usr/bin/env python   

import rospy
from dynamixel_workbench_msgs.srv import DynamixelCommand
import numpy as np
from std_msgs.msg import Float32MultiArray

def motor_enable(motor_id, state):
    rospy.wait_for_service('/dynamixel_workbench/dynamixel_command')
    try:
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        response = dynamixel_command('', motor_id, 'Torque_Enable', state)
        if response.comm_result:
            rospy.loginfo("Motor %d is now enabled!", motor_id)
        return response.comm_result
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)
        return False

def set_dynamixel_position(motor_id, position):
    rospy.wait_for_service('/dynamixel_workbench/dynamixel_command')
    try:
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        response = dynamixel_command('', motor_id, 'Goal_Position', position)
        return response.comm_result
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)
        return False

# Callback to set motor position based on received angle
def callback(msg):
    motor_id = 10  # You can remove the global if not necessary
    motor_angle_rad = msg.data[0]  # Angle in radians
    motor_angle_deg = np.degrees(motor_angle_rad)  # Convert to degrees
    motor_angle_encod = motor_angle_deg / 0.088  # Convert to encoder position (based on your gear ratio)

    # Round to integer
    motor_angle_encod = int(motor_angle_encod)

    rospy.loginfo("Setting motor %d to position %d", motor_id, motor_angle_encod)
    
    # Send the position to the motor
    if not set_dynamixel_position(motor_id, motor_angle_encod):
        rospy.logerr("Failed to set motor position.")

    motor_id = 11  # You can remove the global if not necessary
    motor_angle_rad = msg.data[1]  # Angle in radians
    motor_angle_deg = np.degrees(motor_angle_rad)  # Convert to degrees
    motor_angle_encod = motor_angle_deg / 0.088  # Convert to encoder position (based on your gear ratio)

    # Round to integer
    motor_angle_encod = int(motor_angle_encod)

    rospy.loginfo("Setting motor %d to position %d", motor_id, motor_angle_encod)
    
    # Send the position to the motor
    if not set_dynamixel_position(motor_id, motor_angle_encod):
        rospy.logerr("Failed to set motor position.")

def main():
    # Initialize ROS node
    rospy.init_node('dynamixel_position_control_node')

    # Ensure that the service is available before starting
    rospy.wait_for_service('/dynamixel_workbench/dynamixel_command')
    
    # Create the subscriber once, not in a loop
    rospy.Subscriber('/float_values', Float32MultiArray, callback)

    # Enable the motor
    motor_id = 10
    motor_on = 1
    if not motor_enable(motor_id, motor_on):
        rospy.logerr("Motor enable failed.")

    motor_id = 11
    motor_on = 1
    if not motor_enable(motor_id, motor_on):
        rospy.logerr("Motor enable failed.")
    # Spin and keep the node running
    rospy.spin()

if __name__ == '__main__':
    main()
