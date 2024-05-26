from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mov_cli.plugins import PluginHookData

from .scraper import FilesScraper

plugin: PluginHookData = {
    "version": 1, 
    "scrapers": {
        "DEFAULT": FilesScraper
    }
}

__version__ = "1.1.1"