from threading import Thread
import time
import logging
import cv2
import numpy as np
from matplotlib import pyplot as plt
from camera import Camera

sleep_rate = 0.1
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
num_buckets = 5

class FrontCamera:
    def __init__(self, front_camera):
        # start camera
        self.front_camera = front_camera

        # run that thread
        Thread(target=self.updateFront, args=()).start()
        logging.debug("front cam ingest thread started")

    def getSlice(self, image, i):
        height, width = image.shape[:2]
        bits_per_bucket = height/num_buckets
        return image[bits_per_bucket*i:bits_per_bucket*(i+1), 0:width]

    def processFrontImage(self, image, line_r, line_g, line_b):
        for i in range(num_buckets):
            front_slice = self.getSlice(image, i)
            #cv2.imshow('slice ' + str(i), front_slice)
            combined = np.average(front_slice, axis=0)
            line_b[i][0].set_ydata(combined[:,0])
            line_g[i][0].set_ydata(combined[:,1])
            line_r[i][0].set_ydata(combined[:,2])
        # front_gray = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)
        # front_gray_edge = cv2.Canny(front_gray, 100, 50)
        # cv2.imshow('frame', front_gray_edge)

    def updateFront(self):
        # get everything setup for plotting
        plt.ion()
        fig = plt.figure()
        ax = []
        line_r = []
        line_g = []
        line_b = []
        for i in range(num_buckets):
            ax.append(fig.add_subplot(num_buckets, 1, i+1))
            line_r.append(ax[i].plot(range(640), range(640), 'r'))
            line_g.append(ax[i].plot(range(640), range(640), 'g'))
            line_b.append(ax[i].plot(range(640), range(640), 'b'))

        while(True):
            fresh, front = self.front_camera.read()
            if (fresh):
                logging.debug("front cam ingest update")
                cv2.imshow('narrow', front)
                self.processFrontImage(front, line_r, line_g, line_b)
                fig.canvas.draw()
            time.sleep(sleep_rate)
