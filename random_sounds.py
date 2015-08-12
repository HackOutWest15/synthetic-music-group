import pygame
import random

class Random:
    def __init__(self):
        files = ['dada.wav', 'na-hehehe2.wav', 'shh.wav', 'vatten2.wav', 'knack.wav', 'na2.wav', 'skarpt.wav']
        self.sounds = [pygame.mixer.Sound('Sounds/random/%s' % x) for x in files]
    def play(self, midi_note):
        r = random.randint(1,len(self.sounds))
        self.sounds[r - 1].play()
