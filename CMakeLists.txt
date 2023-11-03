cmake_minimum_required(VERSION 3.0.2)
project(testbed_lin_actuator)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS
    scripts/lin_actuator_server.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
