import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


cid = "13264910862e4cff999bbed9305aeb83"
secret = "4905f294aedf4134a3f1df9816d695f5"

os.environ['SPOTIPY_CLIENT_ID'] = cid
os.environ['SPOTIPY_CLIENT_SECRET'] = secret
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8000/spotify/callback/'

username = "ajeager227"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit=10, offset=0, time_range='long_term')
    for song in range(10):
        list = []
        list.append(results)
        with open('top50_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
else:
    print("Can't get token for", username)

with open('top50_data.json') as f:
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

      all_songs_saved = all_songs.to_csv('top50_songs.csv')

      descending_order = all_songs['artist'].value_counts().sort_values(ascending=False).index
      ax = sb.countplot(y=all_songs['artist'], order=descending_order)

      sb.despine(fig=None, ax=None, top=True, right=True, left=False, trim=False)
      sb.set(rc={'figure.figsize': (6, 7.2)})

      ax.set_ylabel('')
      ax.set_xlabel('')
      ax.set_title('Songs per Artist in Top 50', fontsize=16, fontweight='heavy')
      sb.set(font_scale=1.4)
      ax.axes.get_xaxis().set_visible(False)
      ax.set_frame_on(False)

      y = all_songs['artist'].value_counts()
      for i, v in enumerate(y):
          ax.text(v + 0.2, i + .16, str(v), color='black', fontweight='light', fontsize=14)

      plt.savefig('top50_songs_per_artist.jpg', bbox_inches="tight")

      popularity = all_songs['popularity']
      artists = all_songs['artist']

      plt.figure(figsize=(10, 6))

      ax = sb.boxplot(x=popularity, y=artists, data=all_songs)
      plt.xlim(20, 90)
      plt.xlabel('Popularity (0-100)')
      plt.ylabel('')
      plt.title('Song Popularity by Artist', fontweight='bold', fontsize=18)
      plt.savefig('top50_artist_popularity.jpg', bbox_inches="tight")
