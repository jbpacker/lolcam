import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import sleep

from camera import Camera
from front_camera import FrontCamera
from rear_camera import RearCamera

run_front = True
run_rear = True

white = (255, 255, 255)
black = (0, 0, 0)

if run_front:
    front_camera = Camera(src=1)
    front_cam_processing = FrontCamera(front_camera)

if run_rear:
    back_camera = Camera(src=0)
    rear_cam_processing = RearCamera(back_camera)

def drawPoints(image, point_array):
    for point in point_array:
        cv2.circle(image, point, 2, white, -1)

def main():
    while(True):
        sleep(.1)
        # points = []
        # points.append((20,20))
        # points.append((100, 100))
        # drawPoints(front, points)
    
        # edges = cv2.Canny(back, 220, 210)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
