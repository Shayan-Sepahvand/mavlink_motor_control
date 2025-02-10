1) cd to catkin workspace and git clone the following branch:

```bash
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/dynamixel-workbench.git 
```


2) use catkin_make to build the package

```bash
catkin_make
```

3) Connect the motor baord to the jetson.


4) this are from the following guid: https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/ 

```bash
sudo cp ./99-dynamixel-workbench-cdc.rules /etc/udev/rules.d/ 

sudo udevadm control --reload-rules

sudo udevadm trigger
```

5) The following will search for the dynamixel motors id and baudrate:

```bash
rosrun dynamixel_workbench_controllers find_dynamixel /dev/ttyUSB0
```

6) Connect via the vscode

7) Create a ros package for motor controll that uses the scripts and launch files of the dynamixel

```bash
catkin_create_pkg motor_control std_msgs rospy
```
```bash
rosservice call /dynamixel_workbench/dynamixel_command "command: ''
id: 10
addr_name: 'Torque_Enable'
value: 0" 
```

```bash
rosservice call /dynamixel_workbench/dynamixel_command "command: ''
id: 10
addr_name: 'Operating_Mode'
value: 3" 
comm_result: True
```
