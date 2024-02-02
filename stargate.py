from machine import Pin, ADC
from neopixel import NeoPixel
import time
import random

# Define the ring pin number (2) and number of LEDs (12)
ring=NeoPixel(Pin(2), 12)

# Create a list of the LEDs to use
chevrons_paire = [6,10,4]
chevrons_impaire = [8,2]
chevrons=[6,8,10,2,4]
anneau= [7,9,11,0,1,3,5]

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)


def tour_clock():
    for x in anneau:
        ring [x]=(0,0,2)
        ring.write()
        time.sleep(0.5)

def tour_anticlock():
    for x in reversed (anneau):
        ring [x]=(0,0,2)
        ring.write()
        time.sleep(0.5)


def reset_tour():
    for x in reversed (anneau):
        ring [x]=(0,0,0)
        ring.write()
        
def ouverture():
    for x in anneau:
        ring [x]=(0,0,2)
        ring.write()
        
def blast_ouverture():
    for x in anneau:
        ring [x]=(0,0,20)
        ring.write()   
    

for i in chevrons:
    if i in chevrons_paire:
        tour_clock()
        time.sleep(0.75)
        ring[i]=(30,2,0)
        ring.write()
        time.sleep(0.5)
        ring[i]=(70,7,0)
        ring.write()
        time.sleep(0.5)
        reset_tour()
        time.sleep(0.5)
    if i in chevrons_impaire:
        tour_anticlock()
        time.sleep(0.75)
        ring[i]=(30,2,0)
        ring.write()
        time.sleep(0.5)
        ring[i]=(70,7,0)
        ring.write()
        time.sleep(0.5)
        reset_tour()
        time.sleep(0.5)

ouverture()
time.sleep(0.05)
blast_ouverture()
time.sleep(1)
ouverture() 