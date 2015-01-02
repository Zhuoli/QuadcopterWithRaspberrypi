#!/usr/bin/python
import time
import picamera

FRAMES=500
def capture_frame(frame):
    with picamera.PiCamera() as cam:
        cam.capture('../webserver/webapps/ROOT/data/imgs/image.jpg')

# Capture the images
for frame in range(FRAMES):
    # Note the time before the capture
    start = time.time()
    capture_frame(frame)
    time.sleep(0.1)
