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

# This shows a simple example of waiting for a message to be published.

import paho.mqtt.client as mqtt
from NeuroPy import NeuroPy
import time
from time import sleep
from tqdm import tqdm

neuropy = NeuroPy("COM5",57600) 
neuropy.start()
att = tqdm(total=100, desc="attention", position=1)
med = tqdm(total=100, desc="Meditation", position=0)
volume = [ 50, 50, 50, 50, 50]
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

def attention_callback(value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    #print ("Value of attention is: ", attention_value)
    volume.append(value)
    volume.pop(0)
    att.update(value)
    att.refresh()
    att.update(-value)
    value = 0
    for v in volume:
        value = value + v
    value = value / len(volume)
    return None
def meditation_callback(value):
    volume.append(value)
    volume.pop(0)
    med.update(value)
    med.refresh()
    med.update(-value)
    value = 0
    for v in volume:
        value = value + v
    value = value / len(volume)
    return None
# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client("Neurosky")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
mqttc.on_log = on_log
mqttc.connect("192.168.1.2", 1883, 60)

mqttc.loop_start()

Jalan = True 
Straight = True
Reverse = True

Stop = False
SStop = False
RStop = False

try:
    while True:
        neuropy.setCallBack("attention", attention_callback)
        neuropy.setCallBack("meditation", meditation_callback)
        time.sleep(0.1)

        if Jalan == True:
                    if Straight == True:
                        if neuropy.attention > 75:
                            mqttc.publish("Mindwave", "forward", qos=2)
                            Straight = False
                            Jalan = False
                            Stop = True
                            SStop = True
                    if Reverse == True:
                        if neuropy.meditation > 90:
                            mqttc.publish("Mindwave", "reverse", qos=2)
                            Reverse = False
                            Jalan = False
                            Stop = True
                            RStop = True
        elif Stop == True:
                    if SStop == True:
                        if neuropy.attention < 75:
                            mqttc.publish("Mindwave", "stop", qos=2)
                            SStop = False
                            Stop = False
                            Jalan =True
                            Straight = True
                    if RStop == True:
                        if neuropy.meditation < 90:
                            mqttc.publish("Mindwave", "stop", qos=2)
                            RStop = False
                            Stop = False
                            Jalan = True
                            Reverse = True

finally:
    neuropy.stop()
    




