import network
import time
from machine import unique_id

from umqtt.simple import MQTTClient

WIFI_SSID = "TVOJA_WIFI"
WIFI_PASSWORD = "TVOJE_HESLO"

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
TOPIC = b"iotstich/demo/classroom"


def wifi_connect(ssid, password, timeout_sec=15):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if wlan.isconnected():
        return wlan

    print("Pripajam sa na Wi-Fi:", ssid)
    wlan.connect(ssid, password)

    start = time.time()
    while not wlan.isconnected() and (time.time() - start) < timeout_sec:
        time.sleep(1)
        print(".", end="")
    print()

    if not wlan.isconnected():
        raise RuntimeError("Wi-Fi pripojenie zlyhalo")

    print("Wi-Fi OK, IP:", wlan.ifconfig()[0])
    return wlan


def on_message(topic, msg):
    try:
        print("[SUB]", topic.decode(), "->", msg.decode())
    except Exception:
        print("[SUB]", topic, "->", msg)


def main():
    wifi_connect(WIFI_SSID, WIFI_PASSWORD)

    client_id = b"iotstich-" + unique_id()
    client = MQTTClient(client_id, MQTT_BROKER, port=MQTT_PORT, keepalive=30)
    client.set_callback(on_message)

    print("Pripajam sa na MQTT broker", MQTT_BROKER)
    client.connect()
    print("MQTT pripojene")

    client.subscribe(TOPIC)
    print("Subscribed na topic:", TOPIC)

    counter = 0
    while True:
        # Spracuj prijate spravy
        client.check_msg()

        # Publish testovacej spravy
        payload = "Ahoj z IoT Stich, counter={}".format(counter)
        client.publish(TOPIC, payload)
        print("[PUB]", payload)

        counter += 1
        time.sleep(5)


main()
