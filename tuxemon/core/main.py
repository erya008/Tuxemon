#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (C) 2014, William Edwards <shadowapex@gmail.com>,
#                     Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon.
#
# Tuxemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tuxemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Tuxemon.  If not, see <http://www.gnu.org/licenses/>.
#
# Contributor(s):
#
# William Edwards <shadowapex@gmail.com>
#
#
# core.main Sets up the states and main game loop.
#
from collections import namedtuple
from functools import partial
from . import prepare
from core.components.game_event import *
from .speech import SpeechThread

import threading
from threading import Timer

def worker():
    while(1):
        print 'BAMF'
    return;

def adapter(name, *args):
    nt = namedtuple(name, "parameters")

    def func(*args):
        return nt(args)

    return func


def main():
    """Add all available states to our scene manager (tools.Control)
    and start the game using the pygame interface.

    :rtype: None
    :returns: None

    """
    import pygame
    from .control import PygameControl

    prepare.init()
    control = PygameControl(prepare.ORIGINAL_CAPTION)
    control.auto_state_discovery()
    control.push_state("StartState")
    control.push_state("SplashState")
    control.push_state("FadeInTransition")

    import random
    from core.components.event.actions.player import Player
    control.player1 = prepare.player1

    # code to make this work
    add_monster = partial(adapter("add_monster"))
    Player().add_monster(control, add_monster('txmn_bigfin', 10), 0)
    Player().add_monster(control, add_monster('txmn_rockitten', 10), 0)

    add_item = partial(adapter("add_item"))
    Player().add_item(control, add_item('item_capture_device', 50), 0)
    Player().add_item(control, add_item('item_capture_device', 50), 0)
    Player().add_item(control, add_item('item_capture_device', 50), 0)
    Player().add_item(control, add_item('item_capture_device', 50), 0)
    Player().add_item(control, add_item('item_capture_device', 50), 0)
    Player().add_item(control, add_item('item_super_potion', 20), 0)
    Player().add_item(control, add_item('item_super_potion', 20), 0)
    Player().add_item(control, add_item('item_super_potion', 20), 0)
    Player().add_item(control, add_item('item_super_potion', 20), 0)
    Player().add_item(control, add_item('item_super_potion', 20), 0)

    


    # def TEST_FUNC():
    #     print("this is working")
    #     pygame.event.Event(MOVE_EVENT, move_list = ["S", "S", "E", "W", "N"])
    #
    # t = Timer(15, TEST_FUNC)
    # t.start();

    # block of code useful for testing
    if 0:
        import random
        from core.components.event.actions.player import Player

        add_monster = partial(adapter("add_monster"))
        Player().add_monster(control, add_monster('Bigfin', 10))
        Player().add_monster(control, add_monster('Dollfin', 10))
        Player().add_monster(control, add_monster('Rockitten', 10))
        Player().add_monster(control, add_monster('Nut', 10))
        Player().add_monster(control, add_monster('Sumobug', 10))

        add_item = partial(adapter("add_item"))
        Player().add_item(control, add_item(u'Potion', 1))
        Player().add_item(control, add_item(u'Super Potion', 1))
        Player().add_item(control, add_item(u'Capture Device', 1))

        control.push_state("MonsterMenuState")

        for monster in control.player1.monsters:
            monster.hp = 100
            monster.current_hp = random.randint(1, 2)

    # from core.components.event.actions.combat import Combat
    # start_battle = partial(adapter("random_encounter"))
    # Combat().random_encounter(control, start_battle(1))

    # do not call fade out, the splash screen will do that
    # control.push_state("SplashState")
    # control.push_state("FadeInTransition")

    # # Show the splash screen if it is enabled in the game configuration
    # if prepare.CONFIG.splash == "1":
    #     control.push_state("FadeOutTransition")
    #     control.push_state("StartState")
    #     # control.push_state("FadeInTransition")

    control.main()
    pygame.quit()


def headless():
    """Sets up out headless server and start the game.

    :rtype: None
    :returns: None

    """
    from .control import HeadlessControl

    control = HeadlessControl()
    control.auto_state_discovery()
    control.push_state("HeadlessServerState")
    control.main()
