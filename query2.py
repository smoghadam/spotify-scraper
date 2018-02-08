#####
# query2.py
# Returns releases by an artist
# Adapted from: https://github.com/plamere/spotipy/blob/master/examples/simple1.py
#####

import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Access tokens
client_id = "0d95a04638084b27a789a328a8b96362"
client_secret = "34145c4dfee449bd957579189f1cc8ed"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Hard-coding the artist to be Radiohead and the 
# release type to be singles
artist_id = 'spotify:artist:4Z8W4fKeB5YxbusRsdQVPb'
release_type = 'single'

# Don't include the 10 latest releases; 
# don't return more than 20 releases
results = sp.artist_albums(artist_id, release_type, limit=20, offset=10)
releases = results['items']

# Get the results from the API
while results['next']:
    results = sp.next(results)
    releases.extend(results['items'])

# Print all release names
for release in releases:
    print((release['name']))


