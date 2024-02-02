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

# Couleurs utilisées
eteint = (0,0,0)
bleu = (0,0,2)
bleuIntense = (0,0,20)
rouge = (30,2,0)
rougeIntense = (70,7,0)

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)


def tour_clock(liste, couleur):
    for x in liste:
        ring [x]=couleur
        ring.write()
        time.sleep(0.5)

def setAllLeds(liste, couleur):
    for x in liste:
        ring [x]=couleur
        ring.write()
    

for i in chevrons:
    if i in chevrons_paire:
        tour_clock(anneau, bleu)
    else:
        tour_clock(reversed(anneau),bleu)

    time.sleep(0.75)
    ring[i]=rouge
    ring.write()
    time.sleep(0.5)
    ring[i]=rougeIntense
    ring.write()
    time.sleep(0.5)
    setAllLeds(anneau,eteint)
    time.sleep(0.5)

setAllLeds(anneau, bleu)
time.sleep(0.05)
setAllLeds(anneau, bleuIntense)
time.sleep(1)
setAllLeds(anneau, bleu) 
