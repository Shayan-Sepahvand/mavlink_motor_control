#!/usr/bin/env python3   

import rospy
from dynamixel_workbench_msgs.srv import DynamixelCommand
import numpy as np
import time 


def set_dynamixel_position(motor_id, position):
    rospy.wait_for_service('/dynamixel_workbench/dynamixel_command')
    try:
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        response = dynamixel_command('', motor_id, 'Goal_Position', position)
        return response.comm_result
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

def dynamixel_position_control_node():
    
    
    # t = rospy.Time.now()
    # t = t.to_sec()
    # # Example: Set position for motor with ID 1 to 512 (middle position)
    motor_id = 10
    position = -2000 # Adjust this value based on your motor's resolution
    if set_dynamixel_position(motor_id, position):
        rospy.loginfo("Position set successfully for motor ID %d to position %d", motor_id, position)
    else:
        rospy.logerr("Failed to set position for motor ID %d", motor_id)

   

if __name__ == '__main__':
    rospy.init_node('dynamixel_position_control_node', anonymous=True)
    try:
        dynamixel_position_control_node()
    except rospy.ROSInterruptException:
        pass

