# this is a test

import paho.mqtt.client as mqtt
import time
import json
from simplecrypt import encrypt, decrypt
import pickle
from sklearn.cluster import KMeans

def on_message(client, userdata, message):
    fh = open("data_no_cam_laptop_client.txt","a")
    fh.write(message.payload+"\n")
    fh.close()
    #global mqtt_data
    #mqtt_data = json.loads(message.payload)
    print(message.topic + " " + str(message.payload))

if __name__ == "__main__":
    with open("kmeans","rb") as sf:
        kmeans = pickle.load(sf)

    mqtt_data = ''
    name = "laptop"
    topic = "tAxiY7W4P58QH5Oq/living_room/pir"
    broker_address = "iot.eclipse.org"
    client = mqtt.Client(name)
    client.on_message = on_message
    client.connect(broker_address, 1883, 60)

    client.subscribe(topic,qos=0)

    while True:
        client.loop_start()
        time.sleep(1)
        client.loop_stop()
