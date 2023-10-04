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
