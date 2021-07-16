# Overview
This program uses Spotify API to get your top tracks of a selected time frame and combines them into one image.

![An exmaple album art](https://cdn.discordapp.com/attachments/512721045309095936/865715678286970910/unknown.png)


# Running the Program

To run, you will need to log on to Spotify's developer portal. From there you will create an app. With this app you will need to whitelist http://google.com/ (This URI may change depending on your location). Grab your Client Id and Secret and exit out of the portal.

In your terminal, cd into your folder. You will need to install two pips

> pip install Pillow
 
> pip install spotipy

You will create evironmental variables with the vaules from the app. Run these commands:

> SET SPOTIPY_CLIENT_ID=[Client Id]

> SET SPOTIPY_CLIENT_SECRET=[Client Secret]

> SET SPOTIPY_REDIRECT_URI=http://google.com/

If using Apple, replace SET with export and surrond the vaules with apostrophes. 


Run the program, it will prompt you to type your username and the time range you would like to pull from. It will then take you to your Spotify page. Log on, and the program will redirect you to Google. Copy the URL in the task bar and paste the URL back into the program.

Sit back and let the program work! Then ending file will save in the same directory as the python file. 
