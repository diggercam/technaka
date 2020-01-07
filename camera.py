from picamera import PiCamera
from time import sleep


camera = PiCamera()
camera.start_preview()

for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
 

camera.start_preview()
camera.annotate_text = "Technaka"
camera.start_recording('vid{counter:03d}.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()