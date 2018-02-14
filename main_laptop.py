# this is a test
from mqtt_lib import publish_pir_mqtt, subscribe


if __name__ == "__main__":
    while True:
        subscribe("laptop", "tAxiY7W4P58QH5Ow/living_room/pir", "iot.eclipse.org")