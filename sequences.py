import midi
import pygame
from pygame.time import Clock
from midi import events

pib = midi.read_midifile("Paint_It_Black.mid")

pygame.init()
clk = Clock()

track = pib[0]
ticks = 0

def next_noteonevent(current):
    if isinstance(track[current], midi.NoteOnEvent):
        return current
    else:
        return next_noteonevent(current+1)

idx = next_noteonevent(0)
event = track[idx]
ticks = event.tick
data = event.data

def play(data):
    if data[1] == 0:
        print "STOP " + str(data[0])
    else:
        print "START " + str(data[0])

while True:
    ms_passed = clk.tick()

    ticks = ticks - ms_passed

    #print '.',

    if ticks <= 0:
        play(event.data)
        idx = next_noteonevent(idx+1)
        event = track[idx]
        ticks = event.tick
        data = event.data
