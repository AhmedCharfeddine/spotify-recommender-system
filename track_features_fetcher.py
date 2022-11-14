import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from API_KEY import PUBLIC_KEY, PRIVATE_KEY

auth_manager = SpotifyClientCredentials(PUBLIC_KEY, PRIVATE_KEY)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_track_features(track):
    '''
    params:  
        track:  an ID of three different types (Spotify ID, Spotify URI, Spotify URL)
                for more info: https://spotipy.readthedocs.io/en/2.19.0/#ids-uris-and-urls
    
    returns:
        dict that contains the different features for the given track ID
    '''
    res = sp.audio_features(track)[0]
    del res['uri']
    del res['duration_ms']
    del res['track_href']
    del res['type']
    del res['id']
    del res['analysis_url']
    del res['time_signature']
    return res