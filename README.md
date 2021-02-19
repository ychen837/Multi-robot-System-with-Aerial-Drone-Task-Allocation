# MRS_Drone_Sim_Task_Allocation

![alt text](https://github.com/ychen837/MRS_Drone_Sim_Task_Allocation/blob/main/Screenshot%20from%202020-12-04%2000-38-52.png)

Prerequisites:
- Install Ubuntu 18.04
- Install ROS Melodic and related packages following ROS/Gazebo section: https://dev.px4.io/master/en/setup/dev_env_linux_ubuntu.html#sim_nuttx 
- Installing PX4 package following the guides: https://dev.px4.io/master/en/simulation/gazebo.html
- Prepare the Gazebo multi-robot simulation following: https://dev.px4.io/master/en/simulation/multi_vehicle_simulation_gazebo.html
- QGroundController executable

Simulation:

![alt text](https://github.com/ychen837/MRS_Drone_Sim_Task_Allocation/blob/main/demo/online.gif)
- Start the QGroundController App
- Start the Gazebo simulator following https://dev.px4.io/master/en/simulation/multi_vehicle_simulation_gazebo.html
- Initialize each robot by executing task_posctl_test.py in main folder and uav1, uav2
- Once drones are ready, execute either test_task_alloc_online.py or test_task_alloc_offline.py

Executables:
- test_task_alloc_offline.py: type 1 algorithm master node, assigns tasks before starting the simulation; to run this, first initialize uav by running task_posctl_test.
- task_posctl_test.py: drone pose control node, accepts waypoint command from task allocation master, shuts down when master announce mission is completed
- test_task_alloc_online.py: type 2 algorithm, dynamically assign tasks when agents/drones are idling.


Reference:
- PX4 Development Guide: https://dev.px4.io/master/en/
- PX4 Team Andreas Antener, for the drone pose control test
- ROS unittest: http://wiki.ros.org/unittest
