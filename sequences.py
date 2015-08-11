import midi
import pygame
from pygame.time import Clock
from midi import events

pygame.init()
pygame.mixer.init()
C= pygame.mixer.Sound("Sounds/C3.wav")
Cs = pygame.mixer.Sound("Sounds/C#.wav")
D = pygame.mixer.Sound("Sounds/D3.wav")
Ds = pygame.mixer.Sound("Sounds/D#.wav")
E = pygame.mixer.Sound("Sounds/E.wav")
F = pygame.mixer.Sound("Sounds/F3.wav")
Fs = pygame.mixer.Sound("Sounds/F#.wav")
G = pygame.mixer.Sound("Sounds/G3.wav")
Gs = pygame.mixer.Sound("Sounds/g3#.wav")
A = pygame.mixer.Sound("Sounds/A3.wav")
As = pygame.mixer.Sound("Sounds/A3#.wav")
B = pygame.mixer.Sound("Sounds/B3.wav")


pib = midi.read_midifile("Paint_It_Black.mid")

clk = Clock()

track = pib[1]
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

dict = {'60':C, '61':Cs, '62':D, '63':Ds, '64': E, '65': F, '66': Fs, '67': G, '68': Gs, '69': A, '70':As,'71':B};


def play(data):
    if data[1] == 0:
        print "STOP " + str(data[0])
    else:
        print "START " + str(data[0])
        dict[str(data[0])].play()

while True:
    ms_passed = (clk.tick()*1.3)

    ticks = ticks - ms_passed

    #print '.',

    if ticks <= 0:
        play(event.data)
        idx = next_noteonevent(idx+1)
        event = track[idx]
        ticks = event.tick
        data = event.data
