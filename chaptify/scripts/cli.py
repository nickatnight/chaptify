import os

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


class Clk:
    @staticmethod
    def secho(msg: str, fg: str = "green"):
        click.secho(msg, fg=fg)


@click.command()
@click.option("--url", help="Url of YouTube video.")
def main(url: str):
    chaptify = Chaptify(CLIENT_ID, CLIENT_SECRET)
    ytdl_data = chaptify.fetch_youtube(url)
    data = chaptify.process_youtube(ytdl_data)

    if not data:
        Clk.secho(ERROR_FETCH_MSG, "red")
        return

    playlist_id = data.get("playlist_id")
    tracks_to_add = data.get("tracks_to_add")

    if missing_tracks := data.get("missing_tracks"):
        click.echo(
            MISSING_TRACKS_MSG.format(
                tracks="\n".join(
                    [f"{emoji.emojize(':cross_mark:')} {mt}" for mt in missing_tracks]
                )
            )
        )

        if click.confirm("Do you want to still continue?"):
            msg = ADDING_TRACKS_MSG.format(
                tracks=len(tracks_to_add), name=data.get("playlist_name")
            )
            Clk.secho(msg)
            chaptify.playlist_replace_items(playlist_id, tracks_to_add)

            msg = SUCESSFUL_PLAYLIST_CREATION.format(
                collision=emoji.emojize(":collision:"), url=data.get("playlist_url")
            )
            click.echo(msg)

        return

    msg = ADDING_TRACKS_MSG.format(
        tracks=len(tracks_to_add), name=data.get("playlist_name")
    )
    Clk.secho(msg)
    chaptify.playlist_replace_items(playlist_id, tracks_to_add)

    msg = SUCESSFUL_PLAYLIST_CREATION.format(
        collision=emoji.emojize(":collision:"), url=data.get("playlist_url")
    )
    Clk.secho(msg)


if __name__ == "__main__":
    main()
