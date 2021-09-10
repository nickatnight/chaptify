from unittest import mock, TestCase

from click.testing import CliRunner

from chaptify import __version__
from chaptify.const import ERROR_FETCH_MSG
from chaptify.scripts.cli import main


CURRENT_USER_PLAYLIST = {
    "items": [
        {
            "id": "37i9dQZF1E8CaQuNr838oC",
            "name": "test playlist",
        },
    ]
}
USER_PLAYLIST_CREATE = {
    "name": "Hey Julie",
    "id": "1234asdf",
    "external_urls": {"spotify": "test.link"},
}
SEARCH = {"tracks": {"items": [{"id": "16gd1kpz5Vh8g9JTUWg0v7"}]}}
YTDL = {
    "title": "Hey Julie",
    "chapters": [
        {
            "start_time": 0.0,
            "end_time": 246.0,
            "title": "JEREMIAH KANE - RISING DRAGON FIST",
        }
    ],
}
VIDEO_URL = "https://www.youtube.com/watch?v=2b9AqJimM-0"


def test_version():
    assert __version__ == "0.1.0"


@mock.patch("chaptify.chapti.Spotify")
@mock.patch("chaptify.chapti.YoutubeDL.extract_info")
class ChaptifyTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.runner = CliRunner()

    def test_cli_no_continue(self, mock_ytdl, mock_spotify):
        mock_spotify.return_value.current_user_playlists.side_effect = (
            CURRENT_USER_PLAYLIST,
            {"items": list()},
        )
        mock_spotify.return_value.user_playlist_create.return_value = (
            USER_PLAYLIST_CREATE
        )
        mock_spotify.return_value.search.return_value = SEARCH
        mock_ytdl.return_value = YTDL

        result = self.runner.invoke(main, [VIDEO_URL], input="n\n")
        self.assertTrue(result.exit_code == 0)
        self.assertTrue("Do you want to still continue?" in result.output)

    def test_cli_continue(self, mock_ytdl, mock_spotify):
        mock_spotify.return_value.current_user_playlists.side_effect = (
            CURRENT_USER_PLAYLIST,
            {"items": list()},
        )
        mock_spotify.return_value.user_playlist_create.return_value = (
            USER_PLAYLIST_CREATE
        )
        mock_spotify.return_value.search.return_value = SEARCH
        mock_ytdl.return_value = YTDL

        result = self.runner.invoke(main, [VIDEO_URL], input="y\n")
        self.assertTrue(result.exit_code == 0)
        self.assertTrue("Can be viewed here:\n\ntest.link" in result.output)

    def test_no_youtube_data_output(self, mock_ytdl, mock_spotify):
        mock_ytdl.return_value = dict()
        result = self.runner.invoke(main, [VIDEO_URL], input="n\n")
        self.assertTrue(ERROR_FETCH_MSG in result.output)

    def test_missing_tracks_output(self, mock_ytdl, mock_spotify):
        mock_ytdl.return_value = YTDL
        mock_spotify.return_value.search.return_value = dict()
        mock_spotify.return_value.current_user_playlists.side_effect = (
            CURRENT_USER_PLAYLIST,
            {"items": list()},
        )
        mock_spotify.return_value.user_playlist_create.return_value = (
            USER_PLAYLIST_CREATE
        )

        result = self.runner.invoke(main, [VIDEO_URL], input="n\n")
        self.assertTrue(
            "The following 1 track(s) will not added to the playlist:" in result.output
        )
