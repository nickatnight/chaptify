import emoji


DEFAULT_DESCRIPTION = f"""
Made with {emoji.emojize(':red_heart:',variant='emoji_type')}

by nickatnight
"""

MISSING_TRACKS_MSG = """
The following tracks will not added to the playlist:

{tracks}
"""

ADDING_TRACKS_MSG = """
Adding {tracks} track(s) to playlist: {name}
"""

ERROR_FETCH_MSG = """
There was an error with youtube-dl...exiting.
"""
