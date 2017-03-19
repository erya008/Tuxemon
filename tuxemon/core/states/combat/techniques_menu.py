from __future__ import division

import logging
from collections import defaultdict
from functools import partial

import pygame

from core import tools
from core.components.locale import translator
from core.components.menu import PopUpMenu
from core.components.menu.interface import MenuItem
from core.components.menu.menu import Menu
from core.components.sprite import SpriteGroup, MenuSpriteGroup
from core.components.technique import Technique
from core.components.ui.draw import GraphicBox
from core.components.game_event import *

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)


class TechniqueMenuState(Menu):
    """
    Main menu for combat: Fight, Item, Swap, Run

    TODO: there needs to be more general use registers in the combat state to query
          what player is doing what.  there's lots of spaghetti right now.
    """

    def process_event_hook(self, event):
        print("inside tech procc")
        if (event.type == MENU_EVENT and "technique_menu" in event.target_menu):
            print("in the handler!!!!!!!!!!!!")
            self.change_selection(0)
            self.on_menu_selection(self.get_selected_item())
