from  pyechonest import *
config.ECHO_NEST_API_KEY='CPS7RW8QAUIULBBVJ'

paint_it_black = track.track_from_id('spotify:track:78Az0Z1vNJgqv9QSB0ULLV')
dance_of_eternity = track.track_from_id('spotify:track:7FTf3bJuCq5UYHjUwggKNB')

def get_analysis(track):
    url = track.analysis_url
    pass
