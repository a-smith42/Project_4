import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

#the following project includes code wriiten by Ashley Gingeleski from their Data Science blog

client_id = "13264910862e4cff999bbed9305aeb83"
client_secret = "4905f294aedf4134a3f1df9816d695f5"

os.environ['SPOTIPY_CLIENT_ID'] = client_id
os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8000/spotify/callback/'

#username = "ajeager227"
#username = "aliciasmith0703"
username = "21fc7zdqeiwnizxulljjhou2y"
#username = "23g27uaxfwuvhsrs4zx508e5q"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)
#one token, many scopes
#token2 = util.prompt_for_user_token(username, scope_p)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can not get token for: ", username)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit=5, offset=0, time_range='long_term') #timeframe
    for song in range(10):
        list = []
        list.append(results)
        with open('l_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
else:
    print("Can not get token for: ", username)

with open('l_data.json', 'r', encoding='utf-8') as f:
  data = json.load(f)

  list_of_results = data[0]["items"]
  list_of_artist_names = []
  list_of_artist_uri = []
  list_of_song_names = []
  list_of_song_uri = []
  list_of_durations_ms = []
  list_of_explicit = []
  list_of_albums = []
  list_of_popularity = []

  for result in list_of_results:
      result["album"]
      this_artists_name = result["artists"][0]["name"]
      list_of_artist_names.append(this_artists_name)
      this_artists_uri = result["artists"][0]["uri"]
      list_of_artist_uri.append(this_artists_uri)
      list_of_songs = result["name"]
      list_of_song_names.append(list_of_songs)
      song_uri = result["uri"]
      list_of_song_uri.append(song_uri)
      list_of_duration = result["duration_ms"]
      list_of_durations_ms.append(list_of_duration)
      song_explicit = result["explicit"]
      list_of_explicit.append(song_explicit)
      this_album = result["album"]["name"]
      list_of_albums.append(this_album)
      song_popularity = result["popularity"]
      list_of_popularity.append(song_popularity)

      all_songs = pd.DataFrame(
          {'artist': list_of_artist_names,
           'artist_uri': list_of_artist_uri,
           'song': list_of_song_names,
           'song_uri': list_of_song_uri,
           'duration_ms': list_of_durations_ms,
           'explicit': list_of_explicit,
           'album': list_of_albums,
           'popularity': list_of_popularity

           })

      all_songs_saved = all_songs.to_csv('l_songs.csv')

