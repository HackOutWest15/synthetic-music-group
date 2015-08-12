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

    song = midi.read_midifile("Paint_It_Black2.mid")
    clk = Clock()

    our_tracks = [int(x) for x in sys.argv[1:]]

    all_we_need = []

    for track_id in our_tracks:
        track = song[track_id]
        event = track[0]
        tick = event.tick
        all_we_need.append({'track': track,
                            'event_idx': 0,
                            'event': event,
                            'ticks_left': tick,
                            'play': allnotes.play})

    while True:
        ticks_passed = (clk.tick()*1.3)

        if len(all_we_need) == 0:
            break

        for index, track in enumerate(all_we_need):
            advance(track, ticks_passed)

    print "Bye bye"

if __name__ == '__main__':
    main()
