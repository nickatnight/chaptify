from typing import Dict, Union, List, Tuple

from emoji import emojize
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm
from youtube_dl import YoutubeDL

from .const import DEFAULT_DESCRIPTION, REDIRECT_URI, ScopeTypes
from .utils import clean_line


class Chaptify:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str = None,
        scope: str = ScopeTypes.PLAYLIST_MODIFY_PUBLIC,
    ):
        auth_manager = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri or REDIRECT_URI,
            scope=scope,
        )
        self.sp = Spotify(auth_manager=auth_manager)

    def search(self, query: str) -> Union[None, str]:
        """search spotify for track name and return first hit

        :param query:                   search param ie 'No Doubt - Just A Girl'
        :return:                        the id of the track
        """
        resp = self.sp.search(query, limit=1, market="US")
        items = resp.get("tracks", {}).get("items")
        if items:
            return items[0].get("id")
        return None

    def playlist_add_items(self, playlist_id, tracks_to_add: List[str]):
        """append items to a playlist

        :param playlist_id:             id of playlist
        :param tracks_to_add:           list of track ids
        """
        self.sp.playlist_add_items(playlist_id, tracks_to_add)

    def current_user_unfollow_playlist(self, playlist_id: str) -> None:
        """delete playlist by id"""
        self.sp.current_user_unfollow_playlist(playlist_id)

    def playlist_replace_items(
        self, playlist_id: str, tracks_to_add: List[str]
    ) -> None:
        """replace all items in playlist with new ones

        :param playlist_id:             id of playlist
        :param tracks_to_add:           list of track ids
        """
        self.sp.playlist_replace_items(playlist_id, tracks_to_add)

    def user_id(self) -> str:
        """
        :return:                        logged in user id
        """
        return self.sp.me().get("id")

    def check_if_playlist_exists(self, name: str) -> Union[None, Dict]:
        """check if current playlist exists with given name

        :param name:                    name to check
        :return:                        playlist data if exists, None otherwise
        """
        limit = 50
        offset = 0
        playlists = self.sp.current_user_playlists(limit=limit, offset=offset).get(
            "items", list()
        )

        while playlists:
            for playlist in playlists:
                if name == playlist.get("name"):
                    return playlist

            offset += limit
            playlists = self.sp.current_user_playlists(limit=limit, offset=offset).get(
                "items", list()
            )

        return None

    def get_or_create_playlist(self, title: str, url: str) -> Tuple[bool, Dict]:
        """
        :param title:                   playlist title
        :return:                        (bool if created, playlist)
        """
        playlist = self.check_if_playlist_exists(title)
        if playlist:
            return False, playlist

        msg = DEFAULT_DESCRIPTION.format(url=url)

        return True, self.sp.user_playlist_create(
            self.user_id(), title, description=emojize(msg, variant="emoji_type")
        )

    def fetch_youtube(self, url: str) -> Dict:
        """fetch chapter data from youtube

        :param url:                     youtube video url
        :return:                        success/error, youtube-dl data or error message
        """
        ydl_opts = {"noplaylist": True, "quiet": True, "no_warnings": True}
        try:
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
        except Exception:
            return None

        return info_dict

    def process_youtube(self, ytdl_data: Dict) -> Dict:
        """process chapter data from youtube

        :param ytdl_data:               info dict from youtube-dl
        :return:                        payload track data
        """
        missing_tracks = list()
        tracks_to_add = list()
        chapters = ytdl_data.get("chapters")

        if not chapters:
            return None

        with tqdm(iterable=chapters) as pbar:
            for item in pbar:
                track = clean_line(item)
                track_search = " ".join(
                    track.split("-")
                ).lower()  # dumb down for simplicity
                pbar.set_description(f"fetching '{track}'...")

                track_id = self.search(track_search)
                if track_id:
                    tracks_to_add.append(track_id)
                else:
                    missing_tracks.append(track)

            pbar.set_description("Finished.")
        return dict(missing_tracks=missing_tracks, tracks_to_add=tracks_to_add)
