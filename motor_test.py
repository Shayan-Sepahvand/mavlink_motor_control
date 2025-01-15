from pymavlink import mavutil
import time

# Connect to the vehicle (replace with your actual connection, e.g., serial, UDP)
connection_string = '/dev/ttyACM1'  # Replace with your connection string (UDP/Serial)
master = mavutil.mavlink_connection(connection_string)

# Wait for the first heartbeat to confirm the connection
master.wait_heartbeat()
print(f"Heartbeat from system (ID: {master.target_system}, component ID: {master.target_component})")

# Set mode to STABILIZE (No need to arm in STABILIZE mode, this is for manual control)
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_MODE,
    0,  # Confirmation
    mavutil.mavlink.MAV_MODE_STABILIZE_DISARMED,  # Set to STABILIZE and disarmed
    0, 0, 0, 0, 0, 0
)

# Wait for mode change confirmation
print("Vehicle is in STABILIZE mode")


# Control the throttle via servo output (e.g., Servo 1, which controls the motor)
# Servo 1 usually corresponds to throttle control
# Set the throttle PWM to 1500 (neutral) to run the motor
print("Starting motor...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,  # Confirmation
    6,  # Servo channel 1 (adjust this if you use a different channel for throttle)
    1015,  # Neutral PWM value (1500 for most setups, adjust if necessary)
    0, 0, 0, 0, 0  # Additional parameters are unused here
)

# Run the motor for 5 seconds
time.sleep(20)

# Stop the motor by setting throttle to 1000 (minimum)
print("Stopping motor...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
    0,  # Confirmation
    6,  # Servo channel 1 (same as before)
    1000,  # Minimum PWM value to stop the motor
    0, 0, 0, 0, 0  # Additional parameters are unused here
)

# Optionally: Disarm vehicle (optional since we're using STABILIZE mode)
print("Disarming vehicle...")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_MODE,
    0,  # Confirmation
    mavutil.mavlink.MAV_MODE_STABILIZE_DISARMED,  # Set to STABILIZE and disarmed
    0, 0, 0, 0, 0, 0
)

print("Motor test completed!")

# Close connection
master.close()