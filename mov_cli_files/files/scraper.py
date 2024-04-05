from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Generator, Any, Dict, Optional
    from mov_cli import Config
    from mov_cli.http_client import HTTPClient

from mov_cli import utils
from mov_cli.scraper import Scraper
from mov_cli import Single, Metadata, MetadataType
import os
from datetime import datetime

__all__ = ("FilesScraper", )

video_extensions = [".3g2", ".3ga", ".3gp", ".3gpp", ".aac", ".ac3", ".adt", ".adts", ".aif", ".aifc", ".aiff", ".amr", ".asf", ".asx", ".av", ".avi", ".bmp", ".cue", ".dat", ".divx", ".dv", ".dvr-ms", ".eac3", ".evo", ".f4v", ".flac", ".flc", ".fli", ".flv", ".gif", ".gsm", ".ifo", ".ismv", ".ivf", ".m1v", ".m2p", ".m2t", ".m2ts", ".m2v", ".m3u", ".m4a", ".m4b", ".m4p", ".m4v", ".mk3d", ".mkv", ".mod", ".mov", ".mp2", ".mp2v", ".mp3", ".mp4", ".mp4v", ".mpe", ".mpeg", ".mpeg1", ".mpeg2", ".mpeg4", ".mpg", ".mpg2", ".mpv", ".mts", ".mxf", ".nsv", ".nuv", ".oga", ".ogg", ".ogm", ".ogv", ".ogx", ".oma", ".opus", ".pva", ".qt", ".ra", ".ram", ".rm", ".rmvb", ".s3m", ".sdp", ".spx", ".thd", ".tivo", ".tod", ".tp", ".ts", ".tta", ".vob", ".voc", ".vqf", ".w64", ".wav", ".webm", ".wma", ".wmv", ".wv", ".xesc", ".xspf"]

class FilesScraper(Scraper):
    def __init__(self, config: Config, http_client: HTTPClient) -> None:
        self.base_url = None
        super().__init__(config, http_client)

    def search(self, query: str, limit: int = 10) -> Generator[Metadata, Any, None]:
        try:
            files = os.listdir(query)
        except Exception as e:
            self.logger.error(
                "Error while listing files" \
                f"\nError -> {e}"
            )

            return False
        
        valid_video_files = []

        for file in files:
            if file.split(".")[-1] in video_extensions:
                valid_video_files.append(file)
        
        for file in valid_video_files:
            st_ctime = os.stat(os.path.join(query, file)).st_ctime

            create_datetime = datetime.fromtimestamp(st_ctime)

            year = create_datetime.strftime("%Y")

            yield Metadata(
                id = str(os.path.join(query, file)),
                title = file[:-5],
                type = MetadataType.MOVIE,
                year = year
            )
            
    
    def scrape(self, metadata: Metadata, episode: Optional[utils.EpisodeSelector] = None) -> Single:
        return Single(
            metadata.id,
            title = metadata.title,
            referrer = None,
            year = metadata.year
        )

    def scrape_episodes(self, metadata: Metadata, **kwargs) -> Dict[None, int]:
        return {None: 1}