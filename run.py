import cv2
import numpy as np
from matplotlib import pyplot as plt

from camera import Camera

white = (255, 255, 255)
black = (0, 0, 0)

num_buckets = 2

front_camera = Camera(src=1)
back_camera = Camera(src=0)

def drawPoints(image, point_array):
    for point in point_array:
        cv2.circle(image, point, 2, white, -1)

def getSlice(image, i):
    height, width = image.shape[:2]
    bits_per_bucket = height/num_buckets
    return image[bits_per_bucket*i:bits_per_bucket*(i+1), 0:width]

def runFrontCamera(image, line):
    cv2.imshow('narrow', image)
    for i in range(num_buckets):
        front_slice = getSlice(image, i)
        cv2.imshow('slice ' + str(i), front_slice)
        combined = np.average(front_slice, axis=2)
        line[i][0].set_ydata(combined[0])
    # front_gray = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)
    # front_gray_edge = cv2.Canny(front_gray, 100, 50)
    # cv2.imshow('frame', front_gray_edge)

def processRearCamera(image):
    cv2.imshow('wide', image)
    # back_gray = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
    # back_gray_edge = cv2.Canny(back_gray, 100, 50)
    # cv2.imshow('other', back_gray_edge)

def main():
    plt.ion()
    fig = plt.figure()
    ax = []
    line = []
    for i in range(num_buckets):
        ax.append(fig.add_subplot(num_buckets, 1, i+1))
        line.append(ax[i].plot(range(640), range(640)))
        #for c in range(3):
        #    line[
    while(True):
        fresh, front = front_camera.read()
        if (fresh):
            print "[DEBUG] (main): front update"
            runFrontCamera(front, line)
            fig.canvas.draw()
    
        fresh, back = back_camera.read()
        if (fresh):
            print "[DEBUG] (main): back update"
            processRearCamera(back)
    
        # points = []
        # points.append((20,20))
        # points.append((100, 100))
        # drawPoints(front, points)
    
        # edges = cv2.Canny(back, 220, 210)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    front.stop()
    back.stop()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
