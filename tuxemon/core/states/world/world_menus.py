from __future__ import division

import logging
from functools import partial

import pygame


from core import prepare
from core.tools import open_dialog
from core.components.event.actions import core as core_actions
from core.components.menu.interface import MenuItem
from core.components.menu.menu import Menu
from core.components.locale import translator
from core.components.game_event import *
from core.components import save

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)


def adapter(name, *args):
    from collections import namedtuple
    nt = namedtuple(name, "parameters")

    def func(*args):
        return nt(args)

    return func


def add_menu_items(state, items):
    for key, callback in items:
        label = translator.translate(key).upper()
        image = state.shadow_text(label)
        item = MenuItem(image, label, None, callback)
        state.add(item)


class WorldMenuState(Menu):
    """
    Menu for the world state
    """
    shrink_to_items = True    # this menu will shrink, but size is adjusted when opened
    animate_contents = True

    def process_event_hook(self, event):
        if(event.type == MENU_EVENT):
            if(event.menu_item == "open"):
                self.close()
            elif (event.menu_item == "monsters"):
                self.open_monster_menu()
            elif (event.menu_item == "bag"):
                self.game.replace_state("ItemMenuState")
            elif (event.menu_item == "load"):
                self.game.replace_state("LoadMenuState")
            elif (event.menu_item == "save"):
                logger.info("Saving!")

                try:
                    save.save(self.game.player1,
                            self.capture_screenshot(),
                            1,
                            self.game)
                except Exception as e:
                    logger.error("Unable to save game!!")
                    logger.error(e)
                    print(e)
                self.close()
                #self.game.replace_state("SaveMenuState")
            elif (event.menu_item == "exit"):
                core_actions.Core().quit(self.game, None, {})

    def startup(self, *args, **kwargs):
        super(WorldMenuState, self).startup(*args, **kwargs)

        def change_state(state, **kwargs):
            return partial(self.game.replace_state, state, **kwargs)

        def exit_game():
            core_actions.Core().quit(self.game, None, {})

        def not_implemented_dialog():
            open_dialog(self.game, [translator.translate('not_implemented')])

        # Main Menu - Allows users to open the main menu in game.
        menu_items_map = (
            ('menu_journal', not_implemented_dialog),
            ('menu_monster', self.open_monster_menu),
            ('menu_bag', change_state("ItemMenuState")),
            ('menu_player', not_implemented_dialog),
            ('menu_save', change_state("SaveMenuState")),
            ('menu_load', change_state("LoadMenuState")),
            ('menu_options', not_implemented_dialog),
            ('exit', exit_game)
        )
        add_menu_items(self, menu_items_map)


    def open_monster_menu(self):
        from core.states.monster import MonsterMenuState

        def monster_menu_hook():
            """ Used to rearrange monsters interactively

            This is slow b/c forces each slot to be re-rendered.
            Probably not an issue except for very slow systems.

            :return: None
            """
            monster = context.get('monster')
            if monster:
                # TODO: maybe some API for re-arranging menu items
                # at this point, the cursor will have changed
                # so we need to re-arrange the list before it is rendered again
                # TODO: API for getting the game player object
                player = self.game.player1
                monster_list = player.monsters

                # get the newly selected item.  it will be set to previous position
                original_monster = monster_menu.get_selected_item().game_object

                # get the position in the list of the cursor
                index = monster_list.index(original_monster)

                # set the old spot to the old monster
                monster_list[context['old_index']] = original_monster

                # set the current cursor position to the monster we move
                monster_list[index] = context['monster']

                # store the old index
                context['old_index'] = index

            # call the super class to re-render the menu with new positions
            # TODO: maybe add more hooks to eliminate this runtime patching
            MonsterMenuState.on_menu_selection_change(monster_menu)



        def select_first_monster():
            # TODO: API for getting the game player obj
            player = self.game.player1
            monster = monster_menu.get_selected_item().game_object
            context['monster'] = monster
            context['old_index'] = player.monsters.index(monster)
            self.game.pop_state()  # close the info/move menu

        def open_monster_stats():
            open_dialog(self.game, [translator.translate('not_implemented')])

        def open_monster_submenu(menu_item):
            menu_items_map = (
                ('monster_menu_info', open_monster_stats),
                ('monster_menu_move', select_first_monster),
            )
            menu = self.game.push_state("Menu")
            menu.shrink_to_items = True
            add_menu_items(menu, menu_items_map)

        def handle_selection(menu_item):
            if 'monster' in context:
                del context['monster']
            else:
                open_monster_submenu(menu_item)

        context = dict()    # dict passed around to hold info between menus/callbacks
        monster_menu = self.game.replace_state("MonsterMenuState")
        monster_menu.on_menu_selection = handle_selection
        monster_menu.on_menu_selection_change = monster_menu_hook

    def animate_open(self):
        """ Animate the menu sliding in

        :return:
        """
        self.state = "opening"  # required

        # position the menu off screen.  it will be slid into view with an animation
        right, height = prepare.SCREEN_SIZE

        # TODO: more robust API for sizing (kivy esque?)
        # this is highly irregular:
        # shrink to get the final width
        # record the width
        # turn off shrink, then adjust size
        self.shrink_to_items = True     # force shrink of menu
        self.menu_items.expand = False  # force shrink of items
        self.refresh_layout()           # rearrange items
        width = self.rect.width         # store the ideal width

        self.shrink_to_items = False    # force menu to expand
        self.menu_items.expand = True   # force menu to expand
        self.refresh_layout()           # rearrange items
        self.rect = pygame.Rect(right, 0, width, height)  # set new rect

        # animate the menu sliding in
        ani = self.animate(self.rect, x=right - width, duration=.50)
        ani.callback = lambda: setattr(self, "state", "normal")
        return ani

    def animate_close(self):
        """ Animate the menu sliding out

        :return:
        """
        ani = self.animate(self.rect, x=prepare.SCREEN_SIZE[0], duration=.50)
        return ani

#####################################################################################################################
    def capture_screenshot(self):
        screenshot = pygame.Surface(self.game.screen.get_size())
        world = self.game.get_state_name("WorldState")
        world.draw(screenshot)
        return screenshot
