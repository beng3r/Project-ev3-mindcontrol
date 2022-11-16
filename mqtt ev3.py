#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
import paho.mqtt.client as mqtt



# Declare
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)


#For MQTT
MQTT_name = "localhost"
#MQTT_name = "192.168.0.2"
Topic_name = "Mindwave"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Mindwave")

# The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):
    if msg.topic=="Mindwave":
        command_str = str(msg.topic)
        print(str(msg.topic))
        if command_str == 'Neurosky connected':
            print(str(msg.payload))
            tank_pair.on(left_speed=50, right_speed=50)
            
def init_mqtt():
    # Create MQTT client
    mqttClient = mqtt.Client("Ev3")
    mqttClient.on_connect = on_connect
    mqttClient.on_message = on_message
    # mqttClient.on_message = on_disconnect
    # Connect to MQTT server
    try:
        mqttClient.connect(MQTT_name, 1883, 60)
        print("MQTT Server connected")
        MQTT_connection = 0
        mqttClient.loop_start()
    except:
        print("MQTT Server disconnected")
        MQTT_connection = 1
        pass
           