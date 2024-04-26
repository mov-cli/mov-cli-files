from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from mov_cli.utils.platform import SUPPORTED_PLATFORMS

from pathlib import Path
import os

def get_user_media_paths(platform: SUPPORTED_PLATFORMS) -> List[Path]:
    """Returns a list of directories where media is most likely to be stored."""
    paths: List[Path] = []

    if platform == "Linux":
        home_folders = ["Music", "Videos"]

        user_home_dir = Path.home()

        for directory_name in home_folders:
            path = user_home_dir.joinpath(directory_name)

            if path.exists():
                paths.append(path)

    elif platform == "Windows":
        home_folders = ["Music", "Videos"]

        user_home_dir = Path(os.getenv("USERPROFILE"))

        for directory_name in home_folders:
            path = user_home_dir.joinpath(directory_name)

            if path.exists():
                paths.append(path)

    return paths