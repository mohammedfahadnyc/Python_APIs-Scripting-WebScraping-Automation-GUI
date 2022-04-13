from bs4 import BeautifulSoup
import os
import requests
import spotipy



#Getting Date, And Scraping For Songs On That Day
# date = input("Enter a Data in YYYY-MM-DD Format")
date = "2020-02-01"
# year = date.split("-")[0]
link = f"https://www.billboard.com/charts/hot-100/{date}"

soup = BeautifulSoup(requests.get(url=link).text, "html.parser")
song_name = soup.find_all(name="h3",id="title-of-a-story",class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

song_name_list = [song.getText().strip() for song in song_name]




#Authenticating Spotify sp and user
from spotipy.oauth2 import SpotifyOAuth

date = "2020-02-01"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",show_dialog=True,
                                            cache_path="token.txt"))



user_id = sp.current_user()["id"]




# Searching and  finding uri:
uri_list = []
for i in range(10):
    song = input("name \n")
    result = sp.search(q=f"track:{song} year:{date}", type="track")
    uri = result["tracks"]["items"]["uri"]
    uri_list.append(uri)

# for song in song_name_list:
#     result = sp.search(q=f"track:{song} year:{date}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         uri_list.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")

#Create And Add To Playlist


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)














