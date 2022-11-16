#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.button import Button
from time import sleep
from NeuroPy import NeuroPy
from time import sleep

btn = Button()
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
neuropy = NeuroPy("COM5",57600) 
neuropy.start()

def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return None


while True:
    if neuropy.attention > 70: # Access data through object
        tank_pair.on(left_speed=50, right_speed=50)
    if neuropy.attention < 70:
        tank_pair.off()
        
try:
    while True:
        sleep(0.2)
finally:
    neuropy.stop()
    tank_pair.off()