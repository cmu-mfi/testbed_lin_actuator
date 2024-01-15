# testbed_lin_actuator

## Installation Instructions
1. Install Arduino IDE [here](https://www.arduino.cc/en/software)
2. Add the user to the dialout group and log out and log back in:
    ```bash
    sudo usermod -a -G dialout $(whoami)
    sudo usermod -a -G tty $(whoami)
    ```
3. Upload the Arduino code in the arduino folder onto the Arduino using the Arduino IDE.
4. Install pyserial and numpy packages using the following commands:
    ```bash
    pip install pyserial numpy
    ```

## Running Instructions
1. Start the testbed_linear_actuator server by running:
    ```bash
    rosrun testbed_lin_actuator lin_actuator_server.py
    ```
2. Command the linear actuators by substituting i with [1,2,3,4] depending on the linear actuator you want to raise or lower:
    ```bash
    rostopic pub /toggle std_msgs/Int16 "data: i"
    ```

## Modification Instructions
1. If you want to add additional linear actuators, you will need to plug in additional motors and add another L298N motor controller according to the definitions at the top of the arduino/lin_actuator/lin_actuator.ino file. Then you will also need to change the number of linear actuators variable and increase the size of the arrays for position, velocities, etc that are initialized with the number of linear actuators variable. 
2. Next you will need to add additional maximum and minimum values for each new linear actuator by first adding 0.0 to the minimum position array and 0.01 to the maximum position array in the src/LinearActuator.py and the scripts/lin_actuator_server.py files.
3. Finally, you should toggle each new linear actuator and adjust the maximum and minimum limits by monitoring the /linear_actuator_joint_states topic.
