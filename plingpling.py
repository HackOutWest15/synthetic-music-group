'''
LOL
'''

tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
files = ['Sounds/GlasPling/%s.wav' % x for x in tones]
sounds = []

def init():
    sounds = [pygame.mixer.Sound(x) for x in files]


def play(midi_note):
    sounds[(midi_note - 60) % 12
