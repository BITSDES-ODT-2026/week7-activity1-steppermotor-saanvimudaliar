from machine import Pin
import time

in1 = Pin(5, Pin.OUT)
in2 = Pin(12, Pin.OUT)
in3 = Pin(25, Pin.OUT)
in4 = Pin(19, Pin.OUT)

cw = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
acw = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

t = 1

while True:
    for x in range(500):
        for s in cw:
            in1.value(s[0])
            in2.value(s[1])
            in3.value(s[2])
            in4.value(s[3])
            time.sleep(t)
            
    time.sleep(t)
        
    for x in range(500):
        for s in acw:
            in1.value(a[0])
            in2.value(a[1])
            in3.value(a[2])
            in4.value(a[3])
            time.sleep(t)
            
    time.sleep(t)
