from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
from threading import Thread
import argparse
import imutils
import cv2
import datetime

class WebcamVideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        if self.stopped:
            return

        (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

class FPS:
    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        self._end = datetime.datetime.now()

    def update(self):
        self._numFrames += 1

    def elapsed(self):
        return (self._end - self._start).total_seconds()

    def fps(self):
        return self._numFrames / self.elapsed()

def main():
    print("startup")
    vs = WebcamVideoStream(src=0).start()
    fps = FPS().start()
    
    while fps._numFrames < 100:
        print(fps._numFrames)
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
    
        cv2.imshow("Frame", frame)
    
        fps.update()
    
    fps.stop()
    
    cv2.destroyAllWindows()
    vs.stop()

if __name__ == "__main__":
    main()
