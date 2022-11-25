from djitellopy import tello
from time import sleep

me = tello.Tello()

# We should be connected to Drone WiFi First
me.connect()

# get_battery() returns the Charging percentage of Drone
print(me.get_battery())

# Drone will take off with this command
me.takeoff()

sleep(10)

# # Left-Right Forward-Backward Up-Down Yaw
# me.send_rc_control(0, 50, 0, 0)
#
# # To Put Drone To Sleep for 2 seconds
# sleep(1)
#
# me.send_rc_control(0, -50, 0, 0)
#
# sleep(1)
#
# # Drone will move right for 2 seconds
# me.send_rc_control(30, 0, 0, 0)
# sleep(1)
#
#
# me.send_rc_control(-30, 0, 0, 0)
# sleep(1)

# me.send_rc_control(0, 0, 0, 0)

me.land()

