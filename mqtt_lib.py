import paho.mqtt.client as mqtt
import time
import json


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


def subscribe(name,topic,broker_address):
    client = mqtt.Client(name)
    print("creating new instance: ",name)
    client.on_message = on_message
    client.connect(broker_address)
    print("connecting to broker: ",broker_address)

    client.loop_start()
    client.subscribe(topic)
    print("subscribing to topic: ",topic)
    time.sleep(4)
    client.loop_stop()


def publish_pir_mqtt(name,topic,broker_address,payload):
    client = mqtt.Client(name)
    print("creating new instance: ",name)
    client.connect(broker_address)
    print("connecting to broker: ",broker_address)
    client.publish(topic, json.dumps(payload))
    print("publishing message to topic: ",topic)

