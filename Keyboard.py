# HRI
# RGB LED for HR-OS1
#git push
import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *
#Establish Pins

GPIO.setmode(GPIO.BCM)

LED_Red = 2
LED_Green = 3
LED_Blue = 4

GPIO.setup(LED_Red, GPIO.OUT)
GPIO.setup(LED_Green, GPIO.OUT)
GPIO.setup(LED_Blue, GPIO.OUT)

GPIO.output(LED_Red, True)
GPIO.output(LED_Green, True)
GPIO.output(LED_Blue, True)


def display(color):
    GPIO.setwarnings(False)
    if (color == 'red'):
        GPIO.output(LED_Red, False)
        GPIO.output(LED_Green, True)
        GPIO.output(LED_Blue, True)
    elif (color == 'green'):
        GPIO.output(LED_Red, True)
        GPIO.output(LED_Green, False)
        GPIO.output(LED_Blue, True)
    elif (color == 'blue'):
        GPIO.output(LED_Red, True)
        GPIO.output(LED_Green, True)
        GPIO.output(LED_Blue, False)
    elif (color == 'white'):
        GPIO.output(LED_Red, False)
        GPIO.output(LED_Green, False)
        GPIO.output(LED_Blue, False)
    elif (color == 'off'):
        GPIO.output(LED_Red, True)
        GPIO.output(LED_Green, True)
        GPIO.output(LED_Blue, True)
display('off') 

for x in range (0, 10):
	display('blue')
	time.sleep(3)
	display('red')
	time.sleep(3)
display('off')
