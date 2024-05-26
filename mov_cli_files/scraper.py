from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict, Optional, Generator, Any
    from mov_cli import Config

    from mov_cli.utils import EpisodeSelector
    from mov_cli.http_client import HTTPClient
    from mov_cli.scraper import ScraperOptionsT

from mov_cli.scraper import Scraper
from mov_cli.utils import what_platform
from mov_cli import Single, Metadata, MetadataType

from thefuzz import fuzz
from datetime import datetime

from .paths import get_user_media_paths
from pathlib import Path

__all__ = ("FilesScraper",)

video_extensions = [".3g2", ".3ga", ".3gp", ".3gpp", ".aac", ".ac3", ".adt", ".adts", ".aif", ".aifc", ".aiff", ".amr", ".asf", ".asx", ".av", ".avi", ".bmp", ".cue", ".dat", ".divx", ".dv", ".dvr-ms", ".eac3", ".evo", ".f4v", ".flac", ".flc", ".fli", ".flv", ".gif", ".gsm", ".ifo", ".ismv", ".ivf", ".m1v", ".m2p", ".m2t", ".m2ts", ".m2v", ".m3u", ".m4a", ".m4b", ".m4p", ".m4v", ".mk3d", ".mkv", ".mod", ".mov", ".mp2", ".mp2v", ".mp3", ".mp4", ".mp4v", ".mpe", ".mpeg", ".mpeg1", ".mpeg2", ".mpeg4", ".mpg", ".mpg2", ".mpv", ".mts", ".mxf", ".nsv", ".nuv", ".oga", ".ogg", ".ogm", ".ogv", ".ogx", ".oma", ".opus", ".pva", ".qt", ".ra", ".ram", ".rm", ".rmvb", ".s3m", ".sdp", ".spx", ".thd", ".tivo", ".tod", ".tp", ".ts", ".tta", ".vob", ".voc", ".vqf", ".w64", ".wav", ".webm", ".wma", ".wmv", ".wv", ".xesc", ".xspf"]

class FilesScraper(Scraper):
    def __init__(self, config: Config, http_client: HTTPClient, options: Optional[ScraperOptionsT] = None) -> None:
        self.platform = what_platform()
        super().__init__(config, http_client, options)

    def search(self, query: str, _: int = 20) -> Generator[Metadata, Any, None]:
        options_path = self.options.get("path", None)
        media_paths = get_user_media_paths(self.platform)

        if options_path is not None:
            options_path = Path(options_path)

            if options_path.exists():
                media_paths = [options_path]

        for media_path in media_paths:
            paths = media_path.glob("**/*")

            for path in paths:
                if fuzz.token_set_ratio(path.name, query) < 30 and query != "*":
                    continue

                if path.suffix not in video_extensions:
                    continue

                st_ctime = path.stat().st_ctime

                create_datetime = datetime.fromtimestamp(st_ctime)

                year = create_datetime.strftime("%Y")

                yield Metadata(
                    id = str(path), 
                    title = path.stem, 
                    type = MetadataType.SINGLE, 
                    year = year
                )

    def scrape(self, metadata: Metadata, _: EpisodeSelector) -> Single:
        return Single(
            url = metadata.id, 
            title = metadata.title, 
            year = metadata.year 
        )

    def scrape_episodes(self, _: Metadata) -> Dict[None, int]:
        return {None: 1}