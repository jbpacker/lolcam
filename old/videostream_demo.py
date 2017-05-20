from video_stream import VideoStream
import datetime
import argparse
import imutils
import time
import cv2

vs = VideoStream().start()
time.sleep(2)

while (True):
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    timestamp = datetime.datetime.now()
    ts = timestampe.strftime("%A %d %B %Y %I:%M:%S%p")

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
