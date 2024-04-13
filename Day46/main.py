import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from secret_key import CLIENT_ID_SPOTIFY, CLIENT_SECRET_SPOTIFY

date = input("Which year do you want to travel to? Type the date in this format YYY-MM-DD:")
# date = "2000-08-12"
# print(date)

URL = "https://www.billboard.com/charts/hot-100/"
URL = URL + date + "/"
print(URL)

response = requests.get(URL)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# movies = soup.find_all(name="h3", class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

songs = soup.select(selector="li li h3") 

song_name_list = []
for song_tag in songs:
    song = song_tag.get_text()
    song_name_list.append(song)
# print(song_name_list)

song_names = []
for item in song_name_list:
    cleaned_item = item.replace('\t', '').replace('\n', '')
    song_names.append(cleaned_item)
print(song_names)


from spotipy.oauth2 import SpotifyOAuth

# CLIENT_ID_SPOTIFY = "xxxxxxxx"
# CLIENT_SECRET_SPOTIFY = "xxxxxxxx"
URL_REDIRECT = "http://example.com"

spotify = spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID_SPOTIFY, 
    client_secret=CLIENT_SECRET_SPOTIFY, 
    redirect_uri=URL_REDIRECT)
access_token = spotify.get_access_token()


# Create a Spotify API Client
SPOTIPY_CLIENT_ID = CLIENT_ID_SPOTIFY
SPOTIPY_CLIENT_SECRET = CLIENT_SECRET_SPOTIFY
SPOTIPY_REDIRECT_URI = URL_REDIRECT
SPOTIFY_DISPLAY_NAME = 11182423579
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private",
        username=SPOTIFY_DISPLAY_NAME,  # email might also work, I haven't tested it
    )
)
user = sp.current_user()
# print(user)
user_id = user["id"]
# print(user_id)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0] # from input
# year = "2020"
# song_names = song_names[0:5] # short song_names list
for song in song_names:
    print(song)
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pprint.pprint(result)
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

top_100 = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=top_100["id"], items=song_uris)