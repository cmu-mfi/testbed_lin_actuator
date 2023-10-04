from LinearActuator import LinearActuator
import numpy as np
import time

la = LinearActuator('/dev/ttyACM0')

print(la.get_joint_positions())

la.reset()
la.wait_until_done_moving()
print(la.get_joint_positions())

p = np.ones((1,2)) * 0.0087
duration = [1.0]
la.move_joint_position(p,duration)
la.wait_until_done_moving()
print(la.get_joint_positions())

la.reset()
la.wait_until_done_moving()
print(la.get_joint_positions())

la.close()