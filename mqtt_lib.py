import paho.mqtt.client as mqtt
import time
import json


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


if __name__ == "__main__":
    # creating a mqtt client instance
    client = mqtt.Client("pir_living_room")
    # attach function to callback
    client.on_message = on_message
    print("creating new instance")
    # connect(host, port=1883, keepalive=60, bind_address="")
    broker_address = "iot.eclipse.org"
    client.connect(broker_address)
    print("connecting to broker")

    client.loop_start()
    client.subscribe("living_room/pir")
    print("subscribing to topic","living_room/pir")
    # publish(topic, payload=None, qos=0, retain=False)
    client.publish("living_room/pir", json.dumps([0,0,0,0,0]))
    print("publishing message to topic","[0,0,0,0,0]")
    time.sleep(4)
    client.loop_stop()