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

video_extensions = ['webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'rrc', 'gifv', 'mng', 'mov', 'avi', 'qt', 'wmv', 'yuv', 'rm', 'asf', 'amv', 'mp4', 'm4p', 'm4v', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'm4v', 'svi', '3gp', '3g2', 'mxf', 'roq', 'nsv', 'flv', 'f4v', 'f4p', 'f4a', 'f4b', 'mod'] 

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