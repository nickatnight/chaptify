<p align="center">
    <a href="#"><img alt="Synthwave" src="https://f4.bcbits.com/img/0017910770_0"></a>
    <small>Photo: https://daily.bandcamp.com</small>
</p>
<p align="center">
    <a href="https://github.com/nickatnight/chaptify/actions"><img alt="GitHub Actions status" src="https://github.com/nickatnight/chaptify/actions/workflows/main.yml/badge.svg"></a>
</p>

# chaptify :closed_book: :speaker:
A simple cli to convert audio from [chapter](https://support.google.com/youtube/answer/9884579?hl=en) enabled YouTube videos to your Spotify playlist

## Reason?
I needed an automated process to transfer 80s synthwave mixes I listen to from [YouTube](https://www.youtube.com/watch?v=2b9AqJimM-0), most of which were chapter enabled (new video feature from YT), to Spotify playlists.

## Install (dev only for now)
This package relies on `spotipy`, a lightweight python wrapper for Spotify api. See their [docs](https://spotipy.readthedocs.io/en/latest/) for installation or Spotify [developer](https://developer.spotify.com/documentation/general/guides/) guide for obtaining api keys

1. clone this repo `$ git clone git@github.com:nickatnight/chaptify.git` and `cd chaptify`
2. export ENV vars
    ```shell
    $ export SPOTIFY_CLIENT_SECRET=<some_secret>
    $ export SPOTIFY_CLIENT_ID=<some_secret>
    ```
3. install in editable mode `$ pip install -e .`
4. run `$ chaptify --url=https://www.youtube.com/watch\?v\=Pz1a9MM-Vn4`

![alt text](https://i.imgur.com/AS3wTbW.gif "chaptify")
