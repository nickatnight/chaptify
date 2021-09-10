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
A simple cli to create Spotify playlists from the audio of [chapter](https://support.google.com/youtube/answer/9884579?hl=en) enabled YouTube videos

## Reason?
I needed an automated process to transfer 80s synthwave mixes I listen to from [YouTube](https://www.youtube.com/watch?v=2b9AqJimM-0), most of which were chapter enabled (new video feature from YT), to Spotify playlists.

## Install (edit mode) Python 3.9+
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
* on first use, `spotipy` will spin up a temporary web server on whatever port is specified above to automatically handle the oauth redirect

## Usage
```bash
Usage: chaptify [OPTIONS] URL

  Youtube video link URL

Options:
  -a, --append TEXT  Append to a playlist (by name).
  --help             Show this message and exit.
```

<!-- https://imgur.com/a/BYHqmhi -->
<p align="center">
    <img alt="cli demo" src="https://i.imgur.com/jVpwvYX.gif">
</p>


## Development
This project uses [Poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) to manage dev environment.  Once installed:
1. follow steps 1-2 from above
2. install packages with `poetry install`
3. black `poetry run black .`
4. flake8 `poetry run flake8`
5. test `poetry run pytest --cov=chaptify tests/`
6. build sdist `poetry build --format sdist`
7. create new setup.py `tar -xvf dist/*-`poetry version -s`.tar.gz -O '*/setup.py' > setup.py`

## Limitations
* obviously, this tool is limited to whats available on Spotify
* only supports US market
* works best with title tracks with variations of "name - artist" eg Rosentwig - Journey
* there is no fancy algorithm or deep learning technique when using spotify search, just fetch me the first hit
