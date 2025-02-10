1) cd to catkin workspace and git clone the following branch:


git clone -b noetic-devel https://github.com/ROBOTIS-GIT/dynamixel-workbench.git 

2) use catkin_make to build the package

catkin_make

3) Connect the motor baord to the jetson.


4) this are from the following guid: https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/ 

sudo cp ./99-dynamixel-workbench-cdc.rules /etc/udev/rules.d/ 

sudo udevadm control --reload-rules

sudo udevadm trigger

5) The following will search for the dynamixel motors id and baudrate:


rosrun dynamixel_workbench_controllers find_dynamixel /dev/ttyUSB0

