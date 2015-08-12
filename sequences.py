import midi
import sys
import pygame
from pygame.time import Clock
from midi import events


def play(event, playfun):
    if isinstance(event, midi.NoteOnEvent) and event.data[1] != 0:
        print "START " + str(event.data[0])
        playfun(event.data[0])
        return False
    elif isinstance(event, midi.EndOfTrackEvent):
        return True

def advance(track, ticks_passed):
    track['ticks_left'] = track['ticks_left'] - ticks_passed

    if track['ticks_left'] <= 0:
        end = play(track['event'], track['play'])
        if end:
            all_we_need.remove(index)
        else:
            track['event_idx'] = track['event_idx'] + 1
            track['event'] = track['track'][track['event_idx']]
            track['ticks_left'] = track['event'].tick

def main():
    pygame.init()
    #pygame.mixer.init()
    pygame.mixer.init(frequency=22050, size=8, channels=2, buffer=2048)

    from all_notes import AllNotes
    allnotes = AllNotes()
    from plingpling import Glaspling
    pling = Glaspling()
    from random_sounds import Random
    random = Random()


    sounds = {'random': random, 'all': allnotes, 'pling': pling}

    if len(sys.argv) <= 4:
        print "Usage: python sequences.py midi_file track1 sound1 track2 sound2 ..."
        print "  available sounds: " + str(sounds.keys())
        sys.exit(1)


    midi_file = sys.argv[1]
    our_tracks = sys.argv[2::2]
    our_sounds = sys.argv[3::2]

    song = midi.read_midifile(midi_file)
    clk = Clock()
    all_we_need = []

    for (tid,soundname) in zip(our_tracks, our_sounds):
        track = song[int(tid)]
        event = track[0]
        tick = event.tick
        sound = sounds.get(soundname, pling)
        all_we_need.append({'track': track,
                            'event_idx': 0,
                            'event': event,
                            'ticks_left': tick,
                            'play': sound.play})

    while True:
        ticks_passed = (clk.tick()*1.3)

        if len(all_we_need) == 0:
            break

        for index, track in enumerate(all_we_need):
            advance(track, ticks_passed)

    print "Bye bye"

if __name__ == '__main__':
    main()
