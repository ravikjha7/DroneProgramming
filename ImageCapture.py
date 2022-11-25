from djitellopy import tello
import cv2 as imageCptr
from matplotlib import pyplot as plt


me = tello.Tello()

# We should be connected to Drone WiFi First
me.connect()

# get_battery() returns the Charging percentage of Drone
print(me.get_battery())

# Switch The Streaming On
me.streamon()


count = 0
while True:
    # To Get The Image Frame By Frame
    img = me.get_frame_read().frame
    # To Resize The Image For Fast Rendering
    img = imageCptr.resize(img, (360, 240))
    # To Save The Image
    imageCptr.imwrite("frame%d.jpg" % count, img)
    # To Display the image in a Window
    imageCptr.imshow("Image", img)
    # To Keep The Image on Window For 1 milli second
    imageCptr.waitKey(1)
    count += 1
