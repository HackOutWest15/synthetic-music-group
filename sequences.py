import midi
import pygame
from pygame.time import Clock

pib = midi.read_midifile("Paint_It_Black.mid")

pygame.init()
clk = Clock()

track = pib[0]
ticks = 0
event = track[0]

while True:
    ms_passed = clk.tick(100)

    ticks = ticks + ms_passed



    print ms_passed
