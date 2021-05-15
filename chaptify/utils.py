import re
from typing import Dict


def clean_line(item: Dict) -> str:
    title = item.get("title")
    matched = re.search(r"\d..", title)

    if ".." not in title:
        return title

    if matched:
        idx = matched.end()
        return title[(idx + 1) :]

    return ""
