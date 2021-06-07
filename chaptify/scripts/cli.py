import os
from typing import Dict

import click
from emoji import emojize

from ..chapti import Chaptify
from ..const import (
    MISSING_TRACKS_MSG,
    ADDING_TRACKS_MSG,
    ERROR_FETCH_MSG,
    SUCESSFUL_PLAYLIST,
    FOUND_ALL_TRACKS,
)


CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def _go(data: Dict, append: str, ch: Chaptify) -> None:
    """helper method for writing to stdout and playlist handling

    :param data:                        processing data
    :param append:                      name of spotify playlist to append to
    param ch:                           Chaptify instance
    """
    playlist_id = data.get("id")
    tracks_to_add = data.get("tracks_to_add")
    playlist_name = data.get("name")
    playlist_url = data.get("external_urls", {}).get("spotify", "")

    msg = ADDING_TRACKS_MSG.format(tracks=len(tracks_to_add), name=playlist_name)
    click.echo(msg)

    if append:
        msg = SUCESSFUL_PLAYLIST.format(action="appended to", url=playlist_url)
        ch.playlist_add_items(playlist_id, tracks_to_add)
    else:
        msg = SUCESSFUL_PLAYLIST.format(action="created", url=playlist_url)
        ch.playlist_replace_items(playlist_id, tracks_to_add)

    click.echo(emojize(msg))


@click.command()
@click.argument("url")
@click.option("-a", "--append", help="Append to a playlist.")
def main(url: str, append: str):
    """
    :param url:                         youtube url of video
    :param append:                      name of spotify playlist to append tracks to
    """
    data = dict()
    chaptify = Chaptify(CLIENT_ID, CLIENT_SECRET)
    fetch_data = chaptify.fetch_youtube(url)
    process_data = chaptify.process_youtube(fetch_data)
    msg = FOUND_ALL_TRACKS

    if not process_data:
        click.secho(ERROR_FETCH_MSG, "red")
        return

    title = append or fetch_data.get("title", "")
    playlist_data = chaptify.get_or_create_playlist(title, url)

    data.update(**process_data, **playlist_data)

    if missing_tracks := data.get("missing_tracks"):
        msg = MISSING_TRACKS_MSG.format(
            track_count=len(missing_tracks),
            tracks="\n".join(list(map(lambda s: f":cross_mark: {s}", missing_tracks))),
        )

    # only proceed after user confirmation
    click.echo(emojize(msg))
    if click.confirm("Do you want to still continue?"):
        _go(data, append, chaptify)
    else:
        # delete playlist only if it was newly created
        if not append:
            chaptify.current_user_unfollow_playlist(playlist_data.get("id"))


if __name__ == "__main__":
    main()
