# **********************************************************
# *                                                        *
# * TBODY_DRIVER Ver 0.01                                  *
# * By Rick spooner (spoonie)                              *
# * This is not for vehicle use!!!!!!!!                    *
# * I Take no responsblity if you get Killed or kill       *
# * someone else                                           *
# *                                                        *
# * TO BE USED AS A TEACHING AID ONLY!!!!!!!!!!!!!!!!!     *
# *                                                        *
# *                                                        *
# **********************************************************

import time
import machine
from machine import Pin, PWM
import utime

R_EN = Pin(4, Pin.OUT)
L_EN = Pin(5, Pin.OUT)
R_EN.value(1)
L_EN.value(1)

RPWM = PWM(Pin(10))
LPWM = PWM(Pin(11))

RPWM.freq(3000)
LPWM.freq(3000)

conversion_factor = 3.3 / (65535)

led = Pin(25, Pin.OUT)
led.value(1)

peddle = machine.ADC(28)
tps = machine.ADC(27)

def mapf(val, in_min, in_max, out_min, out_max):
     return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    peddleRead = peddle.read_u16()
    tpsRead = tps.read_u16()
    
    vPeddle = peddleRead * conversion_factor
    vTps = tpsRead * conversion_factor
    
    bPos = mapf(vPeddle, 0, 3.3, 0.45, 2.94)
    
    if bPos < vTps:
        RPWM.duty_u16 (25000)
        LPWM.duty_u16 (0)
    
    elif bPos > vTps:
        LPWM.duty_u16 (25000)
        RPWM.duty_u16 (0)
    
    
    #print("Peddle: ",vPeddle, " ", "TPS: ",vTps)
    #time.sleep(1)