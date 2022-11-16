#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Roger Light <roger@atchoo.org>
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

# This example shows how you can use the MQTT client in a class.

import paho.mqtt.client as mqtt
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B

tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)

class MyMQTTClass(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        processcommand(msg.payload)
        

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        self.connect("localhost", 1883, 60)
        self.subscribe("Mindwave", 0)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc
    
    def forward():
        tank_pair.on(left_speed=50, right_speed=50)
        
    def processcommand(msg):
        if "foward" in message.payload:
            foward()
        else:
            print("No Command")
            tank_pair.stop()

# If you want to use a specific client id, use
# mqttc = MyMQTTClass("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = MyMQTTClass("Ev3")
rc = mqttc.run()


print("rc: "+str(rc))