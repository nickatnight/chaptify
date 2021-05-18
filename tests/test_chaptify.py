from unittest import TestCase

from chaptify import __version__
from . import MockChaptify


def test_version():
    assert __version__ == "0.1.0"


class ChaptifyTestCase(TestCase):
    def setUp(self):
        self.chaptify = MockChaptify()

    def test_process_youtube_new_playlist(self):
        self.chaptify.sp.current_user_playlists.return_value = dict()
        self.chaptify.sp.search.return_value = {"tracks": {"items": [{"id": "jdJ533"}]}}
        self.chaptify.sp.me.return_value = {"id": "JonB"}
        self.chaptify.sp.user_playlist_create.return_value = {
            "id": "XxxxXX",
            "name": "Hey Julie",
            "external_urls": {"spotify": "http://testurl"},
        }
        data = {
            "title": "Hey Julie",
            "chapters": [
                {
                    "start_time": 0.0,
                    "end_time": 246.0,
                    "title": "JEREMIAH KANE - RISING DRAGON FIST",
                }
            ],
        }
        resp = self.chaptify.process_youtube(data)

        self.assertEqual(len(resp.get("missing_tracks")), 0)
        self.assertEqual(len(resp.get("tracks_to_add")), 1)
