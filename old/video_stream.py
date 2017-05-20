# hi, Jef made this?
from webcamvideostream import WebcamVideoStream

class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(800,600),
                 framerate=30):
        if usePiCamera:
            #freak the fuck out
            return
        else:
            self.stream = WebcamVideoStream(src=src)

    def start(self):
        return self.stream.start()

    def update(self):
        return self.stream.update()

    def read(self):
        return self.stream.read()

    def stop(self):
        return self.stream.stop()
