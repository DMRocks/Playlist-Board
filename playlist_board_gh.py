#These things need to be installed
from PIL import Image
import spotipy.util as util

import os
import sys
import json
import spotipy
import webbrowser
import requests
from json.decoder import JSONDecodeError
from collections import OrderedDict


#Learned not to put my client sercet in plain text

#Auth
scope = 'user-top-read'

#Ask for the user to login and use their token
print('Welcome to the album art maker! This will take your 25 most played albums and combine them into one image. ')
print('What is your username?')
username = input()
print(f'Hello, {username}! How recent should we pull from?')
print('')
print('1 - Last 4 weeks.')
print('2 - Last 6 months.')
print('3 - All time.')
print('')
pull_range_int = input()

#Check for what range should be used
if pull_range_int == '1' :
    pull_range_str = 'short_term'
else :      
    if pull_range_int == '2' :
        pull_range_str = 'medium_term'
    else:
        if pull_range_int == '3' :
            pull_range_str = 'long_term'
        else:
            print("Not a 1, 2 or 3 dumbass")
            sys.exit(0)

print('')
print('This program will take you to log in with Spotify; log on. It will take you to Google. Copy and paste the URL (Make sure you copy and paste with the http:// !):')

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

#Spotipy object
sp = spotipy.Spotify(auth=token)

#Talk to Spotify and Get the top tracks from the user
top_tracks = sp.current_user_top_tracks(limit = 100, offset = 0, time_range = pull_range_str)

#Get album art from spotify
image_urls_dup = []
for item in top_tracks["items"] :
  image_urls_dup.append(item["album"]["images"][1]["url"])

#Check for repeats
image_urls = list(OrderedDict.fromkeys(image_urls_dup))

#Mira Expection
if len(image_urls) < 25 :
    print("Whoops! Looks like you havent listen to enough songs to fill out an entire board! Try a boarder scope!")
    sys.exit(0)

#Download 25 images
print("Downloading... This may take a bit.")
for i in range(25):
    response = requests.get(image_urls[i])
    i += 1
    file = open(f"album_art_{i}.png", "wb")
    file.write(response.content)
    file.close()


#Combine the albumb art together into one image
til = Image.new("RGB", (1500, 1500))

i = 0
#This is named e for Ethan <3
for e in range(5):
    for r in range(5): 
        i += 1
        photo_to_copy = Image.open(f"album_art_{i}.png")
        x_cord = 300 * r
        y_cord = 300 * e
        til.paste(photo_to_copy, (x_cord, y_cord))
        os.remove(f"album_art_{i}.png")

til.save(f"{username}_{pull_range_str}.png")
print("Done!")