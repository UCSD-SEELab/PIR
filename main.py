# this is a test
import numpy as np
from pir_lib import pir, cam
from mqtt_lib import publish_pir_mqtt
import time
from datetime import datetime, timedelta


def collect_samples(secs_duration):
    ref_diff = timedelta(0,secs_duration)
    start_time = datetime.now()
    while datetime.now() - start_time < ref_diff:
        pass


if __name__ == "__main__":
    pir = pir([23, 24, 25, 27, 22])
    cam = cam()
    refresh_rate = 0.3

    while True:
        ans = pir.read_pir()
        if not np.all(ans["values"] == [0, 0, 0, 0, 0]):
            name = str(datetime.now())
            cam.take_picture(name)
            publish_pir_mqtt("pir","living_room/pir","iot.eclipse.org",ans)
        time.sleep(0.3)