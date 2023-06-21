import time
import paho.mqtt.client as mqtt

broker_host = "mosquitto"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("pythonapp/prime")

def on_message(client, userdata, msg):
    print("Received message:", msg.payload.decode())

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(broker_host, broker_port, bind_port=21883)
    client.on_connect = on_connect
    client.on_message = on_message

    client.loop_forever()
