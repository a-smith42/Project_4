import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#the following project includes code wriiten by Ashley Gingeleski from their Data Science blog

client_id = "13264910862e4cff999bbed9305aeb83"
client_secret = "4905f294aedf4134a3f1df9816d695f5"

os.environ['SPOTIPY_CLIENT_ID'] = client_id
os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8000/spotify/callback/'

#username = "21fc7zdqeiwnizxulljjhou2y"
username = "aliciasmith0703"
#username = "23g27uaxfwuvhsrs4zx508e5q"
#username = "ajeager227"


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_artists(limit=10, offset=0, time_range='short_term')
    for song in range(10):
        list = []
        list.append(results)
        with open('top10_artists_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
else:
    print("Can't get token for", username)

with open('top10_artists_data.json', 'r', encoding='utf-8') as f:
  data = json.load(f)

  list_of_results = data[0]["items"]

  list_of_artist_names = []
  list_of_artist_uri = []
  list_of_followers = []
  list_of_popularity = []
  list_of_genres = []

  for result in list_of_results:
      this_artists_name = result["name"]
      list_of_artist_names.append(this_artists_name)
      this_artists_uri = result["uri"]
      list_of_artist_uri.append(this_artists_uri)
      this_followers = result["followers"]["total"]
      list_of_followers.append(this_followers)
      this_popularity = result["popularity"]
      list_of_popularity.append(this_popularity)
      this_genres = result["genres"]
      list_of_genres.append(this_genres)

      all_artists = pd.DataFrame(
          {'artist': list_of_artist_names,
           #'artist_uri': list_of_artist_uri,
           'followers': list_of_followers,
           'popularity': list_of_popularity,
           'genres': list_of_genres

           })

      all_artists_saved = all_artists.to_csv('top10_artists.csv')

      #list_string = (" ").join(list_of_genres)
      #list_string = (" ")
      #list_string.join(list_of_genres)
list_string = ' '.join([str(item) for item in list_of_genres])
wordcloud = WordCloud().generate(list_string)
#plt.imshow(wordcloud, interpolation="bilinear")
plt.figure(figsize=[25,20])
plt.imshow(wordcloud, interpolation="bilinear", aspect="auto")
awc = plt.gca()
awc.get_xaxis().set_visible(False)
awc.get_yaxis().set_visible(False)
plt.axis('off')
plt.show()

#TO DO:
#similar artists endpoint
#save top 5 tracks from each artist to playlist