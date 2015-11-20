# HRI
# RGB LED for HR-OS1

import RPi.GPIO
import time

#Establish Pins

GPIO.setmode(GPIO.BCM)

LED_Red = 2
LED_Green = 3
LED_Blue = 4
LED = [LED_Red,LED_Green,LED_Blue]

GPIO.setup(LED_Red, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(LED_Blue, GPIO.OUT)

GPIO.output(LED_Red, 0)
GPIO.output(LED_Green, 0)
GPIO.output(LED_Blue, 0)


def display(self, color):
    if (color == 'red'):
        GPIO.output(LED_Red, true)
        GPIO.output(LED_Green, 0)
        GPIO.output(LED_Blue, 0)
    elif (color == 'green'):
        GPIO.output(LED_Red, 0)
        GPIO.output(LED_Green, true)
        GPIO.output(LED_Blue, 0)
    elif (color == 'blue'):
        GPIO.output(LED_Red, 0)
        GPIO.output(LED_Green, 0)
        GPIO.output(LED_Blue, true)
    elif (color == 'white'):
        GPIO.output(LED_Red, true)
        GPIO.output(LED_Green, true)
        GPIO.output(LED_Blue, true)
    elif (color == 'off'):
        GPIO.output(LED_Red, 0)
        GPIO.output(LED_Green, 0)
        GPIO.output(LED_Blue, 0)
        
        
        



    
