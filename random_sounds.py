import pygame
import random
import glob

class Random:
    def __init__(self):
        files = glob.glob('Sounds/random/*.wav')
        self.sounds = [pygame.mixer.Sound(x) for x in files]

    def play(self, midi_note):
        r = random.randint(1,len(self.sounds))
        self.sounds[r - 1].play()
