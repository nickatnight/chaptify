import os
from typing import Dict

import click
import emoji

from ..chapti import Chaptify
from ..const import (
    MISSING_TRACKS_MSG,
    ADDING_TRACKS_MSG,
    ERROR_FETCH_MSG,
    SUCESSFUL_PLAYLIST_CREATION,
)


CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def _msg(data: Dict, ch: Chaptify):
    """helper method for writing to stdout"""
    msg = ADDING_TRACKS_MSG.format(
        tracks=len(data.get("tracks_to_add")), name=data.get("playlist_name")
    )
    click.secho(msg, "green")
    ch.playlist_replace_items(data.get("playlist_id"), data.get("tracks_to_add"))

    msg = SUCESSFUL_PLAYLIST_CREATION.format(
        collision=emoji.emojize(":collision:"), url=data.get("playlist_url")
    )
    click.echo(msg)


@click.command()
@click.option("--url", help="Url of YouTube video.")
def main(url: str):
    chaptify = Chaptify(CLIENT_ID, CLIENT_SECRET)
    ytdl_data = chaptify.fetch_youtube(url)
    data = chaptify.process_youtube(ytdl_data)

    if not data:
        click.secho(ERROR_FETCH_MSG, "red")
        return

    if missing_tracks := data.get("missing_tracks"):
        click.echo(
            emoji.emojize(
                MISSING_TRACKS_MSG.format(
                    tracks="\n".join(
                        list(map(lambda s: f":cross_mark: {s}", missing_tracks))
                    )
                )
            )
        )

        if click.confirm("Do you want to still continue?"):
            _msg(data, chaptify)
        return

    _msg(data, chaptify)


if __name__ == "__main__":
    main()
