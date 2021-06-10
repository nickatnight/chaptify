DEFAULT_DESCRIPTION = """
YouTube url: {url}

Made with :red_heart:
by nickatnight
"""

MISSING_TRACKS_MSG = """
The following {track_count} track(s) will not added to the playlist:

{tracks}
"""

ADDING_TRACKS_MSG = """
Adding {tracks} track(s) to playlist: {name}
"""

ERROR_FETCH_MSG = """
There was an error with youtube-dl...exiting.
"""

SUCESSFUL_PLAYLIST = """
:collision: Successfully {action} playlist. Can be viewed here:

{url}
"""

FOUND_ALL_TRACKS = """
:check_mark: Great, found all tracks!
"""

SPOTIFY_REDIRECT_URI = "http://localhost:8321"


class ScopeTypes:
    PLAYLIST_MODIFY_PUBLIC = "playlist-modify-public"
