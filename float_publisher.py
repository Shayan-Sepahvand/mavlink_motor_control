

import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray  # Import Float32MultiArray instead of Float32

def publish_floats():
    # Initialize the node
    rospy.init_node('float_publisher', anonymous=True)

    # Create a publisher for a single message containing multiple floats
    pub = rospy.Publisher('float_values', Float32MultiArray, queue_size=1)

    # Set the loop rate (e.g., 30 Hz)
    rate = rospy.Rate(30)

    while not rospy.is_shutdown():  # Check if the node is shutdown
        t = rospy.Time.now().to_sec()
        print(t)

        # Create and populate the float values
        float_value1 = 3.14 * np.sin(t) + 3.14   # Example float 1
        float_value2 = 3.14 * np.sin(t) + 3.14 # Example float 2

        # Create a Float32MultiArray message and set the data
        msg = Float32MultiArray()
        msg.data = [float_value1, float_value2]

        # Publish the message
        pub.publish(msg)

        rospy.loginfo("Published values: %f, %f", float_value1, float_value2)
        
        # Sleep to maintain the loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_floats()
    except rospy.ROSInterruptException:
        rospy.loginfo("Node interrupted and shut down.")
