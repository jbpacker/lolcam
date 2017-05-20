from threading import Thread
import time
import logging
import cv2
import numpy as np
from camera import Camera

sleep_rate = 0.1
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

class RearCamera:
    def __init__(self, rear_camera):
        self.rear_camera = rear_camera

        Thread(target=self.updateRear, args=()).start()
        logging.debug("rear cam ingest thread started")


    def updateRear(self):
        while(True):
            fresh, rear = self.rear_camera.read()
            if fresh:
                logging.debug("rear cam ingest update")
                cv2.imshow('wide', rear)
                # back_gray = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
                # back_gray_edge = cv2.Canny(back_gray, 100, 50)
                # cv2.imshow('other', back_gray_edge)
            time.sleep(sleep_rate)
