from unittest import mock

from chaptify.chapti import Chaptify


class MockChaptify(Chaptify):
    def __init__(self, client_id="test", client_secret="test"):
        self.sp = mock.Mock()
