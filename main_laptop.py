# this is a test

import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print(message.topic + " " + str(message.payload))

if __name__ == "__main__":
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
