from unittest import mock

from click.testing import CliRunner

from chaptify.scripts.cli import main


CURRENT_USER_PLAYLIST = {"items": []}
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


@mock.patch("chaptify.chapti.Spotify")
@mock.patch("chaptify.chapti.YoutubeDL.extract_info")
def test_cli_no_continue(mock_ytdl, mock_spotify):
    mock_spotify.return_value.current_user_playlists.return_value = (
        CURRENT_USER_PLAYLIST
    )
    mock_spotify.return_value.user_playlist_create.return_value = USER_PLAYLIST_CREATE
    mock_spotify.return_value.search.return_value = SEARCH
    mock_ytdl.return_value = YTDL

    runner = CliRunner()
    result = runner.invoke(main, ["http://clirunner.com"], input="n\n")
    assert result.exit_code == 0
    assert "Do you want to still continue?" in result.output


@mock.patch("chaptify.chapti.Spotify")
@mock.patch("chaptify.chapti.YoutubeDL.extract_info")
def test_cli_continue(mock_ytdl, mock_spotify):
    mock_spotify.return_value.current_user_playlists.return_value = (
        CURRENT_USER_PLAYLIST
    )
    mock_spotify.return_value.user_playlist_create.return_value = USER_PLAYLIST_CREATE
    mock_spotify.return_value.search.return_value = SEARCH
    mock_ytdl.return_value = YTDL

    runner = CliRunner()
    result = runner.invoke(main, ["http://clirunner.com"], input="y\n")
    assert result.exit_code == 0
    assert "Can be viewed here:\n\ntest.link" in result.output
