#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2010-2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# Copyright (c) 2010,2011 Roger Light <roger@atchoo.org>
# All rights reserved.

# This shows a simple example of an MQTT subscriber using connect_srv method.

import paho.mqtt.client as mqtt
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B

tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)

def on_connect(mqttc, obj, flags, rc):
    print("Connected to %s:%s" % (mqttc._host, mqttc._port))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if msg.payload.decode() == "forward":
        forward()
    elif msg.payload.decode() == "left":
        reverse()
    elif msg.payload.decode() == "stop":
        stop()
        

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

def forward():
        tank_pair.on(left_speed=50, right_speed=50)

def stop():
    tank_pair.stop()
def reverse():
    tank_pair.on(left_speed=-50, right_speed=-50)
def left():
    tank_pair.on_for_seconds(left_speed=0,right_speed=50, seconds=1, brake=True, block=True)
        


# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client("Ev3")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
mqttc.on_log = on_log
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("Mindwave", 0)


rc = 0
while rc == 0:
    rc = mqttc.loop()

print("rc: "+str(rc))