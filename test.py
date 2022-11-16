from NeuroPy import NeuroPy
import time
import os
import time
from tqdm import tqdm


#att = tqdm(total=100, desc="attention")
#med = tqdm(total=100, desc="meditation")
raw = tqdm(total=1000, desc="raw")

object1=NeuroPy("COM5", 57600)

volume = [ 50, 50, 50, 50, 50]

def attention_callback(value):
    "this function will be called everytime NeuroPy has a new value for attention"
#    os.system("amixer sset 'Master' " + str(value) + "% > /dev/null")
#    att.moveto(value)

#    print
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None


def meditation_callback(value):

    #os.system("amixer sset 'Master' " + str(value) + "% > /dev/null")
    #do other stuff (fire a rocket), based on the obtained value of attention_value
    #do some more stuff
    return None

def rawValue_callback(value):
    print ("Raw: ", value)
    

def blink_cb(value):
    print("Blink ", value)

#set call back:
object1.setCallBack("rawValue", rawValue_callback)
#object1.setCallBack("attention",attention_callback)
#object1.setCallBack("meditation",meditation_callback)
#object1.setCallBack("blinkStrength",blink_cb)
#call start method
object1.start()

try:
    while True:
        time.sleep(0.5)
except:
    print("exit")
    object1.stop()
