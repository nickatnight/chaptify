# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chaptify', 'chaptify.scripts']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0,<9.0.0',
 'colorama>=0.4.4,<0.5.0',
 'emoji>=1.2.0,<2.0.0',
 'spotipy>=2.18.0,<3.0.0',
 'tqdm>=4.60.0,<5.0.0',
 'youtube_dl>=2021.4.26,<2022.0.0']

entry_points = \
{'console_scripts': ['chaptify = chaptify.scripts.cli:main']}

setup_kwargs = {
    'name': 'chaptify',
    'version': '0.1.0',
    'description': 'Convert audio from chapter enabled YouTube videos to your Spotify playlist',
    'long_description': '<p align="center">\n    <a href=""><img alt="Synthwave" src="https://f4.bcbits.com/img/0017910770_0"></a>\n</p>\n\n# chaptify :closed_book: :speaker:\nA simple cli to convert audio from [chapter](https://support.google.com/youtube/answer/9884579?hl=en) enabled YouTube videos to your Spotify playlist\n\n\n## Reason?\nNeeded an automated process to transfer 80s synthwave mixes on I listen to YT, most of which were chapter enabled (new video feature from YT) ei https://www.youtube.com/watch?v=2b9AqJimM-0\n\n\n# Install',
    'author': 'nickatnight',
    'author_email': 'kay.muneee@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nickatnight/chaptify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
