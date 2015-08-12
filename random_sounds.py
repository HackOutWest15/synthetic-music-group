import pygame

class Random:
    def __init__(self):
        files = ['dada.wav', 'na-hehehe2.wav', 'shh.wav', 'vatten2.wav', 'knack.wav', 'na2.wav', 'skarpt.wav']
        self.sounds = [pygame.mixer.Sound('Souns/random/%s' % x) for x in files]
    def play(self, midi_note):
        self.sounds[midi_note % len(self.sounds)].play()
