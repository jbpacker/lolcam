from threading import Thread 
import logging
import cv2
import time

sleep_rate = 0.15
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                   )

class Camera:
    def __init__(self, src=0):
        self.stopped = False
        self.fresh = False
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        Thread(target=self.update, args=()).start()

    def update(self):
        while True:
            if self.stopped:
                return
            (self.grabbed, self.frame) = self.stream.read()
            self.fresh = True
            logging.debug("updated")
            time.sleep(sleep_rate)

    def read(self):
        was_fresh = self.fresh
        self.fresh = False
        return was_fresh, self.frame

    def start(self):
        self.stopped = False

    def stop(self):
        self.stopped = True
        self.stream.release()
