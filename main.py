# this is a test
import numpy as np
from pir_lib import pir, cam
from mqtt_lib import publish_pir_mqtt
import time
from datetime import datetime, timedelta
import pandas


<<<<<<< HEAD
def collect_samples(pir, cam, secs_duration, refresh_rate):
    print("collecting data...")
    ref_diff = timedelta(0, secs_duration)
=======
def collect_samples(pir,cam, cycle, refresh_rate):
    print("collecting data...")
>>>>>>> d13b9a8fc7cad4296df21e011294b4db27d7ac10
    start_time = datetime.now()
    timestamp = str(start_time)
    pir_values = []
    filenames = []
    index = 0
    for _ in range(cycle):
        pir_values.extend(pir.read_pir())
        cam.take_picture(str(index) + ".jpg")
        filenames.append(str(index) + ".jpg")
        index += 1
<<<<<<< HEAD
        time.sleep(0.3)

    fh = open("pir.txt", "a")
    fh.write(timestamp + "|" + ",".join(map(str, pir_values)) + "\n")
=======
        time.sleep(refresh_rate)
    
    fh = open("pir.txt","a")
    fh.write(timestamp+"|"+",".join(map(str,pir_values))+"\n")
>>>>>>> d13b9a8fc7cad4296df21e011294b4db27d7ac10
    fh.close()
    print("make gif")
    cam.make_gif(filenames, timestamp + ".gif")
    return {"values": pir_values, "timestamp": timestamp}


if __name__ == "__main__":
    pir = pir([23, 24, 25, 27, 22])
    cam = cam()
    cycle = 6
    refresh_rate = 0.3

    while True:
        if not np.all(pir.read_pir() == [0, 0, 0, 0, 0]):
<<<<<<< HEAD
            ans = collect_samples(pir, cam, duration, refresh_rate)
            publish_pir_mqtt("pir", "living_room/pir", "iot.eclipse.org", ans)
        else:
=======
            ans = collect_samples(pir,cam,cycle,refresh_rate)
            publish_pir_mqtt("pir","living_room/pir","iot.eclipse.org",ans)
	else:
>>>>>>> d13b9a8fc7cad4296df21e011294b4db27d7ac10
            time.sleep(refresh_rate)
            print("idle")
