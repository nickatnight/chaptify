# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["chaptify", "chaptify.scripts"]

package_data = {"": ["*"]}

install_requires = [
    "click>=8.0.0,<9.0.0",
    "colorama>=0.4.4,<0.5.0",
    "emoji>=1.2.0,<2.0.0",
    "spotipy>=2.18.0,<3.0.0",
    "tqdm>=4.60.0,<5.0.0",
    "youtube_dl>=2021.4.26,<2022.0.0",
]

entry_points = {"console_scripts": ["chaptify = chaptify.scripts.cli:main"]}

setup_kwargs = {
    "name": "chaptify",
    "version": "0.1.0",
    "description": "Convert audio from chapter enabled YouTube videos to your Spotify playlist",
    "long_description": '<p align="center">\n    <a href="#"><img alt="Synthwave" src="https://f4.bcbits.com/img/0017910770_0"></a>\n    <small>Photo: https://daily.bandcamp.com</small>\n</p>\n<p align="center">\n    <a href="https://github.com/nickatnight/chaptify/actions"><img alt="GitHub Actions status" src="https://github.com/nickatnight/chaptify/actions/workflows/main.yml/badge.svg"></a>\n</p>\n\n# chaptify :closed_book: :speaker:\nA simple cli to convert audio from [chapter](https://support.google.com/youtube/answer/9884579?hl=en) enabled YouTube videos to your Spotify playlist\n\n## Reason?\nI needed an automated process to transfer 80s synthwave mixes I listen to from [YouTube](https://www.youtube.com/watch?v=2b9AqJimM-0), most of which were chapter enabled (new video feature from YT), to Spotify playlists.\n\n## Install (dev only for now)\nThis package relies on `spotipy`, a lightweight python wrapper for Spotify api. See their [docs](https://spotipy.readthedocs.io/en/latest/) for installation or Spotify [developer](https://developer.spotify.com/documentation/general/guides/) guide for obtaining api keys\n\n1. clone this repo `$ git clone git@github.com:nickatnight/chaptify.git` and `cd chaptify`\n2. export ENV vars\n    ```shell\n    $ export SPOTIFY_CLIENT_SECRET=<some_secret>\n    $ export SPOTIFY_CLIENT_ID=<some_secret>\n    ```\n3. install in editable mode `$ pip install -e .`\n4. run `$ chaptify --url=https://www.youtube.com/watch\\?v\\=Pz1a9MM-Vn4`\n\n![alt text](https://i.imgur.com/AS3wTbW.gif "chaptify")\n',
    "author": "nickatnight",
    "author_email": "nickkelly.858@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/nickatnight/chaptify",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "entry_points": entry_points,
    "python_requires": ">=3.9,<4.0",
}


setup(**setup_kwargs)
