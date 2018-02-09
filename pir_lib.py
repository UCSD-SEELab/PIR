import numpy as np
import wiringpi as wp
from datetime import datetime
import time
from picamera import PiCamera
import imageio


class pir:
    def __init__(self, pin_pir):
        self.pin_pir = pin_pir
        wp.wiringPiSetupGpio() # use GPIO pin numbering
        for pir in self.pin_pir:
            wp.pinMode(pir, 0) # input

    def read_pir(self):
        ans = {}
        values = []
        for pir in self.pin_pir:
            values.append(wp.digitalRead(pir))
        ans["values"] = values
        ans["timestamp"] = str(datetime.now())
        return ans

class cam:
    def __init__(self):
        self.cam = PiCamera()
        self.cam.framerate = 24
        self.cam.rotation = 270
        self.cam.resolution = (640, 480)
        time.sleep(0.1)

    def record_video(self,secs):
        timestamp = str(datetime.now())
        self.cam.start_recording(timestamp+'.h264', format='h264', quality=23)
        self.cam.annotate_text = timestamp
        time.sleep(secs)
        self.cam.stop_recording()

    def take_picture(self):
        timestamp = str(datetime.now())
        self.cam.capture(timestamp)

    def make_gif(self, filenames):
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        imageio.mimsave(filenames[0]+".gif",images)


if __name__ == "__main__":
    pir = pir([23,24,25,27,22])
    cam = cam()

    if not np.all(pir.read_pir()["values"] == [0, 0, 0, 0, 0]):
        cam.take_picture()
