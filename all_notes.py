import pygame

class AllNotes:
    def __init__(self):
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

        self.notes = {'41': F1, '42': F1s, '43': G1, '44': G1s, '45': A1, '46':A1s,'47':B1,'48':C2, '49':C2s, '50':D2, '51':D2s, '52': E2, '53': F2, '54': F2s, '55': G2, '56': G2s, '57': A2, '58':A2s,'59':B2,'60':C3, '61':C3s, '62':D3, '63':D3s, '64': E3, '65': F3, '66': F3s, '67': G3, '68': G3s, '69': A3, '70':A3s,'71':B3,'72':C4,'73':C4s,'74':D4,'75':D4s,'76':E4,'77':F4};

    def play(self,note):
        self.notes[str(note)].play()
