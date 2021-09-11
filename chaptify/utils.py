import re
from typing import Dict


def clean_line(item: Dict) -> str:
    """parse a line to get character string for searching

    :param item:                        chapter data from TYDL
    :return:                            clean string
    """
    title = item.get("title")
    matched = re.search(r"\d..", title)

    if ".." not in title:
        return title

    # to catch format.. 29..HOME - Are You There
    if matched:
        idx = matched.end()
        digit = title[:2]
        offset = 0

        # add offset if string starts with double digit for string slice when returning
        try:
            int(digit)
            offset = 1
        except:  # noqa
            pass
        return title[(idx + offset) :]

    return ""
