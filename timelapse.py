#!/usr/bin/env python

import picamera
import time

from datetime import datetime

count = 0
TIMELAPSE_TOTAL_DURATION_S = 10 * 60
TIMELAPSE_INTERVAL_S = 10
VIDEO_DURATION_S = 20

with picamera.PiCamera() as camera:
    camera.start_preview()
    for filename in camera.capture_continuous('/home/pi/technaka/img/img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
        time.sleep(TIMELAPSE_INTERVAL_S)
	count += 1
	if count * TIMELAPSE_INTERVAL_S >= TIMELAPSE_TOTAL_DURATION_S:
		break
    camera.stop_preview()

    now = datetime.now()
    file_name = now.strftime("video-%Y-%m-%dr-%H:%M:%S")
    file_name += ".h264"

    camera.start_recording(file_name)
    camera.wait_recording(VIDEO_DURATION_S)
    camera.stop_recording()

