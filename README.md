<p align="center">
    <a href="#"><img alt="Synthwave" src="https://f4.bcbits.com/img/0017910770_0"></a>
    <small>Photo: https://daily.bandcamp.com</small>
</p>
<p align="center">
    <a href="https://github.com/nickatnight/chaptify/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/chaptify/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/nickatnight/chaptify">
        <img src="https://codecov.io/gh/nickatnight/chaptify/branch/master/graph/badge.svg?token=E03I4QK6D9"/>
    </a>
</p>

# chaptify :closed_book: :speaker:
A simple cli to convert audio from [chapter](https://support.google.com/youtube/answer/9884579?hl=en) enabled YouTube videos, to Spotify playlists

## Reason?
I needed an automated process to transfer 80s synthwave mixes I listen to from [YouTube](https://www.youtube.com/watch?v=2b9AqJimM-0), most of which were chapter enabled (new video feature from YT), to Spotify playlists.

## Install (dev only) Python 3.9+
This package relies on `spotipy`, a lightweight python wrapper for Spotify api. See their [docs](https://spotipy.readthedocs.io/en/latest/) for installation or Spotify [developer](https://developer.spotify.com/documentation/general/guides/) guide for obtaining api keys

1. clone this repo `$ git clone git@github.com:nickatnight/chaptify.git` and `cd chaptify`
2. export ENV vars
    ```shell
    $ export SPOTIFY_CLIENT_SECRET=<some_secret>
    $ export SPOTIFY_CLIENT_ID=<some_id>
    $ export SPOTIFY_REDIRECT_URI=<some_uri>  # optional...defaults to http://localhost:8321
    ```
3. install in editable mode `$ pip install -e .`
4. run `$ chaptify https://www.youtube.com/watch\?v\=Pz1a9MM-Vn4`

### Note
* SPOTIFY_REDIRECT_URI environment variable must match the redirect URI added to your application in your [Dashboard](https://developer.spotify.com/dashboard/applications) , this URI does not need to be accessible
* on first use, `spotipy` will spin up a temporary web server on whatever port is specified above to automatically handle the redirect

## Usage
```bash
Usage: chaptify [OPTIONS] URL

  Youtube video link URL

Options:
  -a, --append TEXT  Append to a playlist (by name).
  --help             Show this message and exit.
```

<!-- https://imgur.com/a/BYHqmhi -->
![alt text](https://i.imgur.com/jVpwvYX.gif "chaptify")

## Limitations
* obviously, this tool is limited to whats available on Spotify
* only supports US market currently
* works best with title tracks with variations of "name - artist" eg Rosentwig - Journey
* there is no fancy algorithm or deep learning technique when using spotify search, just fetch me the first hit
