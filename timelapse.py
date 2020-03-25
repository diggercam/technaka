#!/usr/bin/env python

import picamera
import time
import os
import ftplib
import requests
from datetime import datetime

todays_date = datetime.now()
print(todays_date)

count = 0
TIMELAPSE_TOTAL_DURATION_S = 5
TIMELAPSE_INTERVAL_S = 1
VIDEO_DURATION_S = 5
ITERATION_SLEEP_S = 10
SCRIPT_RUNNING_TIME = 5 * 60
SCRIPT_END_TIME = 19
start = time.time()

#Create storing directory
print("Creating storing directory")
todays_dir=str(todays_date.date())
os.chdir('/home/pi/technaka/img/')
os.mkdir(todays_dir)
os.chdir('/home/pi/technaka/video/')
os.mkdir(todays_dir)

print("Starting timelapse")
with picamera.PiCamera() as camera:
    while True:
        #Save timelapse
        camera.resolution = (1920,1080)
        camera.start_preview()
        img_name=os.path.join('/home/pi/technaka/img/',todays_dir,'img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg')
        for filename in camera.capture_continuous(img_name):
            print('Captured %s' % filename)
            time.sleep(TIMELAPSE_INTERVAL_S)
            count += 1
            if count * TIMELAPSE_INTERVAL_S >= TIMELAPSE_TOTAL_DURATION_S:
                break
        #Save video
        print("Starting video")
        count=0
        now = datetime.now()
        file_name = now.strftime("video-%Y-%m-%dr-%H:%M:%S")
        file_name += ".h264"
        video_dir=os.path.join('/home/pi/technaka/video/',todays_dir)
        os.chdir(video_dir)
        camera.start_recording(file_name)
        camera.wait_recording(VIDEO_DURATION_S)
        camera.stop_recording()
        print('Captured 1080p video')

        time.sleep(ITERATION_SLEEP_S) #do a break

        #Check internet
        print("Checking connectivity")
        try:
            if requests.get('https://google.com').ok:
                print("You're Online - Uploading files on server")
                img_dir=os.path.join('/home/pi/technaka/img/',todays_dir)
                os.chdir(img_dir)
                command = "yadfig2"
                os.system(command)
                #os.chdir('/home/pi/technaka/')
                #command = "./ftp.sh"
                #os.system(command)
                break
        except:
            print("You're Offline")

        #exit program at the end of the day and create website files
        if (todays_date.hour) >= SCRIPT_END_TIME :
             print('END of day')
             break
