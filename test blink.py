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
    return None
def rawValue_callback(value):
    print ("Raw: ", value)
    
    
# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.

jalan = True 
berhenti = False
try:
    while True:
        neuropy.setCallBack("rawValue", rawValue_callback)
        rawValue = neuropy.rawValue
        if rawValue < -300: #if the raw level gets above 200, which indicates a spike, start the clock
            print("Blinked")
        


finally:
    neuropy.stop()
