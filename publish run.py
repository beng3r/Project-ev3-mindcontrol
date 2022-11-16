#!/usr/bin/env python3

from NeuroPy import NeuroPy
from time import sleep
import paho.mqtt.client as mqtt

# This is the Publisher

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return None

#----------------------------------------------------------
client = mqtt.Client()
client.connect("192.168.1.2",1883,60)

client.on_connect = on_connect

neuropy = NeuroPy("COM3",57600) 
neuropy.start()

#--------------------------------------------------------
while True:
    if neuropy.attention > 70: # Access data through object
        client.publish("mindwave", "foward")
        
try:
    while True:
        sleep(0.2)
finally:
    neuropy.stop()


client.loop_forever()



neuropy.setCallBack("rawValue", rawValue_callback)
        time.sleep(0.2)
        if jalan == True : 
            if neuropy.rawValue < -300: # Access data through object
                mqttc.publish("Mindwave", "left", qos=2)
                jalan = False 
                berhenti = True
        else:
            if berhenti == True : 
                if neuropy.attention < 50:
                    mqttc.publish("Mindwave", "stop", qos=2)
                    jalan = True 
                    berhenti= False 
mqttc = mqtt.Client("Neurosky")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
mqttc.on_log = on_log
mqttc.connect("192.168.1.2", 1883, 60)

mqttc.loop_start()
