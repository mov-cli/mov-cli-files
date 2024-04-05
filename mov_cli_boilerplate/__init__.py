from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mov_cli.plugins import PluginHookData

from .boilerplate import Boilerplate

plugin: PluginHookData = {
    "version": 1, 
    "scrapers": {
        "DEFAULT": Boilerplate, 
        "boilerplate": Boilerplate,
    }
}

__version__ = "1.0.0"
