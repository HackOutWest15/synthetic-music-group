import midi
import sys
import pygame
from pygame.time import Clock
from midi import events

pygame.init()
#pygame.mixer.init()
pygame.mixer.init(frequency=22050, size=8, channels=2, buffer=2048)

F4= pygame.mixer.Sound("Sounds/Glaspling/F5.wav")
E4= pygame.mixer.Sound("Sounds/Glaspling/E5.wav")
D4s= pygame.mixer.Sound("Sounds/Glaspling/D5#.wav")
D4= pygame.mixer.Sound("Sounds/Glaspling/D5.wav")
C4s= pygame.mixer.Sound("Sounds/Glaspling/C5#.wav")
C4= pygame.mixer.Sound("Sounds/Glaspling/C5.wav")
C3= pygame.mixer.Sound("Sounds/C3.wav")
C3s = pygame.mixer.Sound("Sounds/C#.wav")
D3 = pygame.mixer.Sound("Sounds/D3.wav")
D3s = pygame.mixer.Sound("Sounds/D#.wav")
E3 = pygame.mixer.Sound("Sounds/Glaspling/E4.wav")
F3 = pygame.mixer.Sound("Sounds/Glaspling/F4.wav")
F3s = pygame.mixer.Sound("Sounds/Glaspling/F4#.wav")
G3 = pygame.mixer.Sound("Sounds/Glaspling/G4.wav")
G3s = pygame.mixer.Sound("Sounds/Glaspling/g4#.wav")
A3 = pygame.mixer.Sound("Sounds/Glaspling/A4.wav")
A3s = pygame.mixer.Sound("Sounds/Glaspling/A4#.wav")
B3 = pygame.mixer.Sound("Sounds/Glaspling/B4.wav")
C2= pygame.mixer.Sound("Sounds/C2.wav")
C2s = pygame.mixer.Sound("Sounds/C2#.wav")
D2 = pygame.mixer.Sound("Sounds/D2.wav")
D2s = pygame.mixer.Sound("Sounds/D2#.wav")
E2 = pygame.mixer.Sound("Sounds/E2.wav")
F2 = pygame.mixer.Sound("Sounds/F2.wav")
F2s = pygame.mixer.Sound("Sounds/F2#.wav")
G2 = pygame.mixer.Sound("Sounds/G2.wav")
G2s = pygame.mixer.Sound("Sounds/g2#.wav")
A2 = pygame.mixer.Sound("Sounds/A2.wav")
A2s = pygame.mixer.Sound("Sounds/A2#.wav")
B2 = pygame.mixer.Sound("Sounds/B2.wav")
F1 = pygame.mixer.Sound("Sounds/F1.wav")
F1s = pygame.mixer.Sound("Sounds/F1#.wav")
G1 = pygame.mixer.Sound("Sounds/G1.wav")
G1s = pygame.mixer.Sound("Sounds/g1#.wav")
A1 = pygame.mixer.Sound("Sounds/A1.wav")
A1s = pygame.mixer.Sound("Sounds/A1#.wav")
B1 = pygame.mixer.Sound("Sounds/B1.wav")
base = pygame.mixer.Sound("Sounds/Trummor/bass-2.wav")
closed = pygame.mixer.Sound("Sounds/Trummor/closedhat-1.wav")
kick = pygame.mixer.Sound("Sounds/Trummor/kick-10.wav")
snare = pygame.mixer.Sound("Sounds/Trummor/snare-8.wav")


tones = {'35':base, '40':snare,'41': F1, '42': F1s, '43': G1, '44': G1s, '45': snare, '46':A1s,'47':B1,'48':C2, '49':C2s, '50':D2, '51':D2s, '52': E2, '53': F2, '54': F2s, '55': G2, '56': G2s, '57': A2, '58':A2s,'59':B2,'60':C3, '61':C3s, '62':D3, '63':D3s, '64': E3, '65': F3, '66': F3s, '67': G3, '68': G3s, '69': A3, '70':A3s,'71':B3,'72':C4,'73':C4s,'74':D4,'75':D4s,'76':E4,'77':F4};

def play(event):
    if isinstance(event, midi.NoteOnEvent) and event.data[1] != 0:
        print "START " + str(event.data[0])
        tones[str(event.data[0])].play()


def main():

    song = midi.read_midifile("Paint_It_Black2.mid")
    clk = Clock()

    our_tracks = [0,1]
    all_we_need = []

    for track_id in our_tracks:
        track = song[track_id]
        event = track[0]
        tick = event.tick
        all_we_need.append({'track': track, 'event_idx': 0, 'event': event, 'ticks_left': tick})

    while True:
        ticks_passed = (clk.tick()*1.3)

        for index, track in enumerate(all_we_need):
            track['ticks_left'] = track['ticks_left'] - ticks_passed

            if track['ticks_left'] <= 0:
                play(track['event'])
                track['event_idx'] = track['event_idx'] + 1
                track['event'] = track['track'][track['event_idx']]
                track['ticks_left'] = track['event'].tick

if __name__ == '__main__':
    main()
