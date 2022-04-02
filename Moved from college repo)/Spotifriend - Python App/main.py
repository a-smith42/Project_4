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

#code featured in lines 35-85 are partially based upon code wriiten by Ashley Gingeleski in their Data Science blog
#(referenced in Thesis)

client_id = "13264910862e4cff999bbed9305aeb83"
client_secret = "4905f294aedf4134a3f1df9816d695f5"

os.environ['SPOTIPY_CLIENT_ID'] = client_id
os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8000/spotify/callback/'

#username = "ajeager227" #chad
#username = "21fc7zdqeiwnizxulljjhou2y" #ethan
username = "aliciasmith0703"
#username = "23g27uaxfwuvhsrs4zx508e5q" #lukasz
#username = "31ecpjmov5wt3eqir2idldipkn7i" #dummy acc

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read user-library-read playlist-modify-private playlist-modify-public playlist-read-private ugc-image-upload'
token = util.prompt_for_user_token(username, scope)
#one token, many scopes
#token2 = util.prompt_for_user_token(username, scope_p)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can not get token for: ", username)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit=5, offset=0, time_range='medium_term') #timeframe
    for song in range(10):
        list = []
        list.append(results)
        with open('top5_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
else:
    print("Can not get token for: ", username)

with open('top5_data.json', 'r', encoding='utf-8') as f:
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
           #'artist_uri': list_of_artist_uri,
           'song': list_of_song_names,
           #'song_uri': list_of_song_uri,
           #'duration_ms': list_of_durations_ms,
           'explicit': list_of_explicit,
           'album': list_of_albums,
           'popularity': list_of_popularity
           })

      all_songs_saved = all_songs.to_csv('top_songs.csv')

def create_trend_figs():
      descending_order = all_songs['artist'].value_counts().sort_values(ascending=False).index
      ax = sb.countplot(y=all_songs['artist'], order=descending_order)

      sb.despine(fig=None, ax=None, top=True, right=True, left=False, trim=False)
      sb.set(rc={'figure.figsize': (10, 10)})

      ax.set_ylabel('')
      ax.set_xlabel('')
      ax.set_title('Songs per Artist in Top 5', fontsize=16, fontweight='heavy')
      sb.set(font_scale=1.4)
      ax.axes.get_xaxis().set_visible(False)
      ax.set_frame_on(False)

      y = all_songs['artist'].value_counts()
      for i, v in enumerate(y):
          ax.text(v + 0.2, i + .16, str(v), color='black', fontweight='light', fontsize=14)

      plt.savefig('top5_songs_per_artist.jpg', bbox_inches="tight")

      popularity = all_songs['popularity']
      artists = all_songs['artist']

      plt.figure(figsize=(10, 6))

      ax = sb.boxplot(x=popularity, y=artists, data=all_songs)
      plt.xlim(20, 90)
      plt.xlabel('Popularity (0-100)')
      plt.ylabel('')
      plt.title('Song Popularity by Artist', fontweight='bold', fontsize=18)
      plt.savefig('top5_artist_popularity.jpg', bbox_inches="tight")
#create_trend_figs()
#this is not being used due to the small sample size being used for demo purposes

#FINDING AUDIO FEATURES OF TOP TRACKS TO BE USED FOR DATA VIS#
#print(sp.audio_features(list_of_song_uri))

#f_list.insert(0,sp.audio_features(list_of_song_uri)) #need to amend this to add songs at different index (for loop)
#print(f_list)
#GET TOP 5 TRACK FEATURES#
def get_track_features():
    x = 0
    f_list = []
    for tracks in list_of_song_uri:
        #print("\nFEATURES for " + list_of_song_names[x] + ": ")#
        f_list.append(sp.audio_features(list_of_song_uri))
        #sp.audio_features(list_of_song_uri)
        #print(sp.audio_features(list_of_song_uri))
        #print("****************LIST ITEM****************")
        #f_str = json.dumps(f_list)
        with open('top_5_features.json', 'w', encoding='utf-8') as fl:
            json.dump(f_list, fl, ensure_ascii=False, indent=4)
        #print(f_list)
        #print(f_str)

        with open('top_5_features.json') as fj:
            f_data = json.load(fj)

            list_of_results = f_data[0]
            list_of_d = []
            list_of_e = []
            list_of_a = []
            list_of_v = []
            list_of_s = []
            list_of_l = []

            for result in list_of_results:
                #result["album"]
                this_d = result["danceability"]
                list_of_d.append(this_d)
                this_e = result["energy"]
                list_of_e.append(this_e)
                this_a = result["acousticness"]
                list_of_a.append(this_a)
                this_v = result["valence"]
                list_of_v.append(this_v)
                this_s = result["speechiness"]
                list_of_s.append(this_s)
                this_l = result["liveness"]
                list_of_l.append(this_l)

                #list_of_songs = result["name"]
                #list_of_song_names.append(list_of_songs)

                track_features = pd.DataFrame(
                    {'danceability': list_of_d,
                     'energy': list_of_e,
                     'acousticness': list_of_a,
                     'valence': list_of_v,
                     'speechiness': list_of_s,
                     'liveness': list_of_l

                     })

        x_graph = np.array([0, 1, 2, 3, 4, 5])
        y_graph = np.array([list_of_d[x], list_of_e[x], list_of_a[x], list_of_s[x], list_of_l[x], list_of_v[x]])
        features = ["Danceability", "Energy", "Acousticness", "Speechiness", "Liveness", "Valence"]
        plt.xticks(x_graph, features)
        plt.plot(x_graph, y_graph, linestyle='--', marker='o', color="red")
        plt.ylabel("Feature Values", fontsize=12)
        plt.xlabel("Features of $\it" + list_of_song_names[x] + "$ by $\it" + list_of_artist_names[x] + "$", fontsize=14, )
        plt.show()
        name = "graph" + str(x) + ".png"
        plt.savefig(name)

        x = x + 1
get_track_features()


#CREATE TEMP PLAYLIST TO STORE TOP TRACKS TO BE USED AS RECOMMENDATION SEEDS#
def create_temp_playlist():
    pl_name = "SEED TRACKS"
    sp.user_playlist_create(user=username, name=pl_name, public=False, collaborative=False,description="seed tracks for generating recommendations")

create_temp_playlist()


#RETRIEVE TEMP PLAYLIST ID#
#print(sp.current_user_playlists(1,0))
results = sp.current_user_playlists(1, 0)
#print(results)
pl_list = []
pl_list.append(results)
with open('temp_playlist.json', 'w', encoding='utf-8') as pl:
    json.dump(pl_list, pl, ensure_ascii=False, indent=4)

with open('temp_playlist.json') as t_pl:
    details = json.load(t_pl)
    list_of_results = details[0]["items"]
for result in list_of_results:
    this_playlist_id = result["id"]
    temp_id = this_playlist_id
    #print(temp_id)

#ADD TRACKS TO PLAYLIST#
sp.user_playlist_add_tracks(user=username, playlist_id=temp_id, tracks=list_of_song_uri, position=0)
#above code works for me, investigate authorisation code flow for other users
#print("seeds: ")
#print(list_of_song_uri)


#GENERATE RECOMMENDATIONS BASED ON PLAYLIST SEEDS#
recs = sp.recommendations(seed_tracks=list_of_song_uri, limit=10)
#print("recs:")
#print(recs)
rec_list = []
rec_list.append(recs)
with open('rec_10.json', 'w', encoding='utf-8') as rl:
    json.dump(rec_list, rl, ensure_ascii=False, indent=4)
#recs_saved = rec_list.to_csv('top_5_recommendations.csv')



#DELETE TEMP PLAYLIST#
sp.user_playlist_unfollow(user=username, playlist_id=temp_id)

#GET ID FROM RECOMMENDATIONS#
to_be_added = []
with open('rec_10.json') as r_pl:
    rec_details = json.load(r_pl)
    list_of_recs = rec_details[0]["tracks"]
for result in list_of_recs:
    this_rec_song_id = result["id"]
    rec_id = this_rec_song_id
    #print(rec_id)
    to_be_added.append(rec_id)
    #print(to_be_added)

#CREATE RECOMMENDATION PLAYLIST#
pl_name = "Spotifriend Recommendations"
#pl_name = "Spotifriend Recommendations"
sp.user_playlist_create(user=username, name=pl_name, public=False, collaborative=False,description="Recommended songs based on " + username + "'s top 5 tracks. Created with Spotifriend")

#RETRTIEVE REC PLAYLIST ID#
results = sp.current_user_playlists(1, 0) #gets most recently added playlist
pl_list = []
pl_list.append(results)
with open('rec_10.json', 'w', encoding='utf-8') as pl:
    json.dump(pl_list, pl, ensure_ascii=False, indent=4)

with open('rec_10.json') as t_pl:
    details = json.load(t_pl)
    list_of_results = details[0]["items"]
for result in list_of_results:
    this_playlist_id = result["id"]
    rec_pl_id = this_playlist_id
    #print("playlistID: " + rec_pl_id)

#ADD RECOMMENDED TRACKS TO PLAYLIST#
sp.user_playlist_add_tracks(user=username, playlist_id=rec_pl_id, tracks=to_be_added, position=0)

#ADD COVER IMAGE (SPOTIFRIEND LOGO)#
#work in progress
logo_text = ' '
with open('logo.txt') as t:
    logo_text = t.readlines()
#print(logo_text)
sp.playlist_upload_cover_image(playlist_id=rec_pl_id, image_b64=logo_text)


#https://vishsubramanian.me/spotify-reccs/#:~:text=Per%20the%20official%20docs%20%E2%80%93%20%E2%80%9CRecommendations,together%20with%20pool%20size%20details
