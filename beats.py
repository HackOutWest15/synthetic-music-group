import pygame

class beats:
    def __init__(self):
        
        bass = pygame.mixer.Sound("Sounds/Trummor/bass-2.wav")
        closed = pygame.mixer.Sound("Sounds/Trummor/closedhat-1.wav")
        cough = pygame.mixer.Sound("Sounds/Trummor/cough.wav")
        kick = pygame.mixer.Sound("Sounds/Trummor/kick-10.wav")
        snare = pygame.mixer.Sound("Sounds/Trummor/snare-8.wav")

        self.notes = {'35': bass, '38': cough, '40': sbare, '44': kick, '45': closed};

    def play(self,note):
        self.notes[str(note)].play()
