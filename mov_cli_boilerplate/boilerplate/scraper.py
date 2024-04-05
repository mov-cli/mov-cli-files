from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Generator, Any, Dict, Literal, Optional
    from mov_cli import Config
    from mov_cli.http_client import HTTPClient

from mov_cli import utils
from mov_cli.scraper import Scraper, MediaNotFound
from mov_cli import Series, Movie, Metadata, MetadataType

__all__ = ("Boilerplate", )


class Boilerplate(Scraper):
    def __init__(self, config: Config, http_client: HTTPClient) -> None:
        self.base_url = ...
        super().__init__(config, http_client)

    def search(self, query: str, limit: int = 10) -> Generator[Metadata, Any, None]:
        ...
    
    def scrape_metadata_episodes(self, metadata: Metadata) -> Dict[int, int] | Dict[None, Literal[1]]:
        ...
    
    def scrape(self, metadata: Metadata, episode: Optional[utils.EpisodeSelector] = None) -> Series | Movie:
        ...