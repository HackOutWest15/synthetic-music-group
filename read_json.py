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

def get_highest_pitch(pitch_list):
	return max(pitch_list)
