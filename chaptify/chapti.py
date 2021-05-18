from typing import Dict, Union, List

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
        scop: str = None,
    ):
        auth_manager = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri or REDIRECT_URI,
            scope=scop or ScopeTypes.PLAYLIST_MODIFY_PUBLIC,
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
        playlists = self.sp.current_user_playlists().get("items", list())
        for playlist in playlists:
            if name == playlist.get("name"):
                return playlist
        return None

    def get_or_create_playlist(self, name: str) -> Dict:
        """
        :return:                        playlist if exists, newly created playlist otherwise
        """
        playlist = self.check_if_playlist_exists(name)
        if playlist:
            return playlist
        return self.sp.user_playlist_create(
            self.user_id(), name, description=DEFAULT_DESCRIPTION
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
        title = ytdl_data.get("title")
        playlist = self.get_or_create_playlist(title)
        chapters = ytdl_data.get("chapters")

        if not chapters:
            return None

        pbar = tqdm(chapters)

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

        return dict(
            missing_tracks=missing_tracks,
            tracks_to_add=tracks_to_add,
            playlist_id=playlist.get("id"),
            playlist_name=playlist.get("name"),
            playlist_url=playlist.get("external_urls", {}).get("spotify", ""),
        )
