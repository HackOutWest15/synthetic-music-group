import json
from pprint import pprint


def get_duration_pitches():
	segment_list = []
	with open('paint_it_black.json') as data_file:
		data = json.load(data_file)
		segments = data["segments"]
		for segment in segments:
			segment_list.append((segment["duration"], segment["pitches"]))

	return(segment_list)

def get_duration_highest_pitch():
	segment_list = []
	with open('paint_it_black.json') as data_file:
		data = json.load(data_file)
		segments = data["segments"]
		for segment in segments:
			if segment["loudness_max"] > -25:
				pitches_list = []
				for pitch in segment["pitches"]:
					if pitch > 0.5:
						pitches_list.append(segment["pitches"].index(pitch))

				segment_list.append((segment["start"],segment["duration"], pitches_list))

	#pprint(segment_list)
	return segment_list

def get_duration_real_tones():
	tonelist = ["C", "C#","D", "D#","E","F","F#","G","G#","A","A#","B"]
	newlist = []
	for tuple in get_duration_highest_pitch():
		tones = []
		for tone in tuple[2]:
			tones.append(tonelist[tone])

		newlist.append((tuple[0], tuple[1], tones))
	pprint(newlist)
	return newlist

get_duration_real_tones();