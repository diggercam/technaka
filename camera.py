from picamera import PiCamera
from time import sleep


camera = PiCamera()

with picamera.PiCamera() as camera:
    camera.start_preview()
    sleep(1)
    for filename in camera.capture_continuous('./img/img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
        print('Captured %s' % filename)
        sleep(1)


camera.stop_preview()