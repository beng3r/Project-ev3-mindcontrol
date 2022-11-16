#!/usr/bin/env python3

import paho.mqtt.client as mqtt





# This is the Subscriber

def on_connect(client1, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("Mindwave")

def on_message(client1, userdata, msg):
  if (msg.payload == 'bar'):
      m.on(left_speed=0, right_speed=0)
      print("foward")
    
    
    
client = mqtt.Client("Ev3")
client.connect("localhost",1883,60)
m.run_forever()
client.on_connect = on_connect
client.on_message = on_message


client.loop_forever()