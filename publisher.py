#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher
def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

client1 = mqtt.Client()
client1.connect("192.168.1.2",1883,60)
while True:
    client1.publish("mindwave", "foward")
    print("printed")
    client1.on_publish = on_publish
client1.loop_forever()