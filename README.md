# Overview
This program uses Spotify API to get your top tracks of a selected time frame and combines them into one image.

![An exmaple album art](https://cdn.discordapp.com/attachments/512721045309095936/865715678286970910/unknown.png)


# Running the Program

To run, you will need to log on to Spotify's developer portal. From there you will create an app. With this app you will need to whitelist http://google.com/ (This URI may change depending on your location). Grab your Client Id and Secret and exit out of the portal.

In your terminal, cd into your folder. You will create evironmental variables with the vaules from the app. Run these commands:

> SET SPOTIPY_CLIENT_ID=[Client Id]

> SET SPOTIPY_CLIENT_SECRET=[Client Secret]

> SET SPOTIPY_REDIRECT_URI=http://google.com/

If using Apple, replace SET with export and surrond the vaules with apostrophes. 

Then run the program, it will prompt you to type your username and the time range you would like to pull from. It will then redirect you to a Spotify page. Log on, then it will redirect you to google. In the taskbar copy that link and paste it into the program.

The program will then download the albums and combine them into one image. All done!
