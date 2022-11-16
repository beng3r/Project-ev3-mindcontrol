from NeuroPy import NeuroPy
from time import sleep
import paho.mqtt.client as mqtt

# Start Neurosky Mindwave

#neuropy = NeuroPy("COM5",57600) 
#neuropy.start()

# For MQTT
MQTT_name = "192.168.1.2"
Topic_name = "Mindwave"
mqtt_event = 0
mqtt_connected = False


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Mindwave")
    client.publish("Mindwave", "Neurosky connected")
    
    
    
# Create MQTT client
    mqttClient = mqtt.Client("neurosky")
    mqttClient.on_connect = on_connect
    
    
# mqttClient.on_message = on_message
    try:
        mqttClient.connect(MQTT_name, 1883, 60)  # Connect to MQTT server
        print("MQTT Server connected")
        mqtt_connected = True
        mqttClient.loop_start()
    except:
        print("MQTT Server disconnected")
        mqtt_connected = False
        pass