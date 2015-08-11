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

#track = pib[1]
tracks = [pib[0], pib[1], pib[2], pib[3], pib[4]]
#ticks = 0

def next_noteonevent(current, pib_list):
    if isinstance(pib_list[current], midi.NoteOnEvent):
        return current
    else:
        return next_noteonevent(current+1, pib_list)

idxs = [next_noteonevent(0, tracks[0]), next_noteonevent(0, tracks[1]), next_noteonevent(0, tracks[2]), next_noteonevent(0, tracks[3]), next_noteonevent(0, tracks[4])]

#event = track[idx]
events = [tracks[0][idxs[0]], tracks[1][idxs[1]], tracks[2][idxs[2]], tracks[3][idxs[3]], tracks[4][idxs[4]]]

#ticks = event.tick
ticks = []
for event in events:
	ticks.append(event.tick) 

#data = event.data
#data = []
#for event in events:
#	data.append(event.data)

dict = {'60':C, '61':Cs, '62':D, '63':Ds, '64': E, '65': F, '66': Fs, '67': G, '68': Gs, '69': A, '70':As,'71':B};


def play(data):
    if data[1] == 0:
        print "STOP " + str(data[0])
    else:
        print "START " + str(data[0])
        dict[str(data[0])].play()

while True:
    ms_passed = (clk.tick()*1.3)

    for index, tick in enumerate(ticks):    	
    	ticks[index] = tick - ms_passed

    	#print '.'
    	if tick <= 0:
	        play(events[index].data)
	        idx = next_noteonevent(idxs[index]+1, tracks[index])
	        events[index] = tracks[index][idx]
	        ticks[index] = events[index].tick