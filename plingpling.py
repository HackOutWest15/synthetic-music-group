'''
LOL
'''

import pygame

class Glaspling:
    def __init__(self):
        tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        files = ['Sounds/pling/%s.wav' % x for x in tones]
        self.sounds = [pygame.mixer.Sound(x) for x in files]

    def play(self, midi_note):
        self.sounds[(midi_note - 60) % 12].play()
