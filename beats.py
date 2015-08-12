import pygame

class Trummor:
    def __init__(self):
        
        bass = pygame.mixer.Sound("Sounds/Trummor/bass-2.wav")
        closed = pygame.mixer.Sound("Sounds/Trummor/closedhat-1.wav")
        cough = pygame.mixer.Sound("Sounds/Trummor/cough.wav")
        kick = pygame.mixer.Sound("Sounds/Trummor/kick-10.wav")
        snare = pygame.mixer.Sound("Sounds/Trummor/snare-8.wav")

        self.notes = {'35': bass, '85': kick, '40': snare, '44': kick, '45': closed, '49':snare};

    def play(self,note):
        self.notes[str(note)].play()
