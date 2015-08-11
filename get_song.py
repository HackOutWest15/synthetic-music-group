from  pyechonest import *
config.ECHO_NEST_API_KEY='CPS7RW8QAUIULBBVJ'

paint_it_black_id = 'spotify:track:78Az0Z1vNJgqv9QSB0ULLV'
dance_of_eternity_id = 'spotify:track:7FTf3bJuCq5UYHjUwggKNB'

def get_track(id_):
    return track.track_from_id(id_)

def get_analysis(track):
    import urllib2
    import json
    url = track.analysis_url
    response = urllib2.urlopen(url)
    return json.loads(response.read())
