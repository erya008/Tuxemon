#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (C) 2014, William Edwards <shadowapex@gmail.com>
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
from __future__ import absolute_import

import logging
from collections import namedtuple

from core import prepare
from core import tools
from core.components import item
from core.components import monster
from core.components.event.actions.common import Common

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)


class Player(object):

    def teleport(self, game, action, contexts):
        """Teleport the player to a particular map and coordinates

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: map_name,coordinate_x,coordinate_y

        **Examples:**

        >>> action.__dict__
        {
            "type": "teleport",
            "parameters": [
                "map1.tmx",
                "5",
                "5"
            ]
        }

        """
        # Get the player object from the game.
        player = game.player1
        world = game.current_state

        # Get the teleport parameters for the position x,y and the map to load.
        mapname = str(action.parameters[0])
        position_x = int(action.parameters[1])
        position_y = int(action.parameters[2])

        # If we're doing a screen transition with this teleport, set the map name that we'll
        # load during the apex of the transition.
        # TODO: This only needs to happen once.
        if world.in_transition:
            world.delayed_mapname = mapname

        # Check to see if we're also performing a transition. If we are, wait to perform the
        # teleport at the apex of the transition
        if world.in_transition:
            world.delayed_teleport = True
            # Set the global_x/y variables based on the player's pixel position and the tile size.
            world.delayed_x = player.position[0] - (position_x * player.tile_size[0])
            world.delayed_y = player.position[1] - (position_y * player.tile_size[1]) + player.tile_size[1]
        # If we're not doing a transition, then just do the teleport
        else:
            # Set the global_x/y variables based on the player's pixel position and the tile size.
            world.global_x = player.position[0] - (position_x * player.tile_size[0])
            world.global_y = player.position[1] - (position_y * player.tile_size[1]) + player.tile_size[1]

            map_path = prepare.BASEDIR + "resources/maps/" + mapname
            if map_path != world.current_map.filename:
                world.change_map(map_path)

        # Stop the player's movement so they don't continue their move after they teleported.
        player.moving = False


    def delayed_teleport(self, game, action, contexts):
        """ Set teleport information.  Teleport will be triggered during screen transition

        Only use this if followed by a transition

        :param game: core.control.Control
        :param action: Tuple
        :return: None
        """
        # Get the world object from the game.
        world = game.current_state

        # give up if there is a teleport in progress
        if world.delayed_teleport:
            return

        # Get the teleport parameters for the position x,y and the map to load.
        mapname = str(action.parameters[0])
        position_x = int(action.parameters[1])
        position_y = int(action.parameters[2])

        world.delayed_mapname = mapname
        world.delayed_teleport = True

        # Get the player object from the game.
        player = game.player1

        # Set the global_x/y variables based on the player's pixel position and the tile size.
        world.delayed_x = player.position[0] - (position_x * player.tile_size[0])
        world.delayed_y = player.position[1] - (position_y * player.tile_size[1]) + player.tile_size[1]


    def transition_teleport(self, game, action, contexts):
        """Combines the "teleport" and "screen_transition" actions to perform a teleport with a
        screen transition. Useful for allowing the player to go to different maps.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: map_name,coordinate_x,coordinate_y,transition_time_in_seconds

        **Examples:**

        >>> action.__dict__
        {
            "type": "transition_teleport",
            "parameters": [
                "map1.tmx",
                "5",
                "5",
                "2",
                "2"
            ]
        }

        """
        # Get transition parameters
        transition_time = action.parameters[3]

        # Start the screen transition
        screen_transition = game.event_engine.actions["screen_transition"]["method"]
        Action = namedtuple("action", ["type", "parameters"])
        transition_action = Action(action.type, [transition_time])
        screen_transition(game, transition_action, contexts)

        # set the delayed teleport
        self.delayed_teleport(game, action, contexts)


    def add_monster(self, game, action, contexts):
        """Adds a monster to the current player's party if there is room. The action parameter
        must contain a monster slug to look up in the monster database.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: monster_slug

        **Example:**

        >>> action.__dict__
        {
            "type": "add_monster",
            "parameters": [
                "Bulbatux",
                "10"
            ]
        }

        >>> monster = core.components.monster.Monster()
        >>> monster.load_from_db(action[1])
        ...
        >>> pprint.pprint(monster.__dict__)
        ... {'attack': 50,
        ...  'attack_modifier': [u'1', u'1.1', u'1.2'],
        ...  'back_battle_sprite': u'resources/gfx/sprites/battle/bulbatux-back.png',
        ...  'body': <core.components.fusion.Body instance at 0x2d0b3f8>,
        ...  'defense': 7,
        ...  'defense_modifier': [u'1', u'1.1', u'1.2'],
        ...  'front_battle_sprite': u'resources/gfx/sprites/battle/bulbatux-front.png',
        ...  'hp': 30,
        ...  'hp_modifier': [u'0.9', u'1', u'1.1'],
        ...  'level': 0,
        ...  'menu_sprite': u'resources/gfx/sprites/battle/bulbatux-menu01.png',
        ...  'moves': [],
        ...  'name': u'Bulbatux',
        ...  'special_attack': 9,
        ...  'special_attack_modifier': [u'1', u'1.1', u'1.2'],
        ...  'special_defense': 8,
        ...  'special_defense_modifier': [u'1', u'1.1', u'1.2'],
        ...  'speed': 7,
        ...  'speed_modifier': [u'1', u'1.1', u'1.2'],
        ...  'status': 'Normal',
        ...  'type1': u'grass',
        ...  'type2': u'poison'}
        ...
        >>> game.player1.add_monster(monster)
        >>> game.player1.monsters
        ... [<core.components.monster.Monster instance at 0x2d0b3b0>]

        """
        monster_slug = action.parameters[0]
        monster_level = action.parameters[1]
        current_monster = monster.Monster()
        current_monster.load_from_db(monster_slug)
        current_monster.set_level(int(monster_level))

        game.player1.add_monster(current_monster)


    def set_monster_health(self, game, action, contexts):
        """Changes the hp of a monster in the current player's party. The action parameters
        may contain a monster slot and the amount of health. If no slot is specified,
        all monsters are healed. If no health is specified, the hp is maxed out.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: slot,health

        **Example:**

        >>> action.__dict__
        {
            "type": "set_monster_health",
            "parameters": [
                "0",
                "1"
            ]
        }
        """
        if not game.player1.monsters > 0:
            return

        monster_slot = action.parameters[0]
        monster_health = action.parameters[1]

        if monster_slot:
            if len(game.player1.monsters) < int(monster_slot):
                return

            monster = game.player1.monsters[int(monster_slot)]
            if monster_health:
                monster.current_hp = int(monster.hp * min(1, max(0, float(monster_health))))
            else:
                monster.current_hp = monster.hp
        else:
            for monster in game.player1.monsters:
                if monster_health:
                    monster.current_hp = int(monster.hp * min(1, max(0, float(monster_health))))
                else:
                    monster.current_hp = monster.hp


    def set_monster_status(self, game, action, contexts):
        """Changes the status of a monster in the current player's party. The action parameters
        may contain a monster slot and the new status to be appended. If no slot is specified,
        all monsters are modified. If no status is specified, the status is cleared.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: slot,status

        **Example:**

        >>> action.__dict__
        {
            "type": "set_monster_status",
            "parameters": [
                "0",
                "status_poison"
            ]
        }
        """
        if not game.player1.monsters > 0:
            return

        monster_slot = action.parameters[0]
        monster_status = action.parameters[1]

        if monster_slot:
            if len(game.player1.monsters) < int(monster_slot):
                return

            monster = game.player1.monsters[int(monster_slot)]
            if monster_status:
                monster.status.append(monster_status)
            else:
                monster.status = []
        else:
            for monster in game.player1.monsters:
                if monster_status:
                    monster.status.append(monster_status)
                else:
                    monster.status = []


    def set_monster_level(self, game, action, contexts):
        """Changes the level of a monster in the current player's party. The action parameters
        may contain a monster slot and the amount by which to level. If no slot is specified,
        all monsters are leveled. If no level is specified, the level is reverted to 1.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: slot,level

        **Example:**

        >>> action.__dict__
        {
            "type": "set_monster_level",
            "parameters": [
                "0",
                "1"
            ]
        }
        """
        if not game.player1.monsters > 0:
            return

        monster_slot = action.parameters[0]
        monster_level = action.parameters[1]

        if monster_slot:
            if len(game.player1.monsters) < int(monster_slot):
                return

            monster = game.player1.monsters[int(monster_slot)]
            if monster_level:
                monster.level = max(1, monster.level + int(monster_level))
            else:
                monster.level = 1
        else:
            for monster in game.player1.monsters:
                if monster_level:
                    monster.level = max(1, monster.level + int(monster_level))
                else:
                    monster.level = 1


    def add_item(self, game, action, contexts):
        """Adds an item to the current player's inventory. The action parameter must contain an
        item name to look up in the item database.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        **Example:**

        >>> action.__dict__
        {
            "type": "add_item",
            "parameters": [
                "Potion"
            ]
        }

        """
        player = game.player1
        item_to_add = item.Item(action.parameters[0])

        # If the item already exists in the player's inventory, add to its quantity, otherwise
        # just add the item.
        if item_to_add.slug in player.inventory:
            player.inventory[item_to_add.slug]['quantity'] += 1
        else:
            player.inventory[item_to_add.slug] = {'item': item_to_add, 'quantity': 1}


    def player_face(self, game, action, contexts):
        """Makes the player face a certain direction.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: direction

        Action parameter can be: "left", "right", "up", or "down"
        """

        # Get the parameters to determine what direction the player will face.
        direction = action.parameters[0]

        # If we're doing a transition, only change the player's facing when we've reached the apex
        # of the transition.
        if game.current_state.in_transition:
            game.current_state.delayed_facing = direction
        else:
            game.player1.facing = direction


    def player_stop(self, game, action, contexts):
        """Makes the player stop moving.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: None

        """
        # Get a copy of the world state.
        world = game.get_state_name("WorldState")
        if not world:
            return

        world.menu_blocking = True


    def player_resume(self, game, action, contexts):
        """Makes the player resume movement.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: None

        """
        # Get a copy of the world state.
        world = game.get_state_name("WorldState")
        if not world:
            return

        world.menu_blocking = False

    def set_player_attribute(self, game, action, contexts):
        """Sets the given attribute of the player character to the given value.
        Valid Parameters: attribute, value
        
        **Example:**

        >>> action.__dict__
        {
            "type": "set_player_attribute",
            "parameters": [
                "party_limit",
                "8"
            ]
        }
        """
        world = game.get_state_name("WorldState")
        if not world:
            return

        attribute = action.parameters[0]
        value = action.parameters[1]
        
        Common.set_character_attribute(world.player1, attribute, value)

    def modify_player_attribute(self, game, action, contexts):
        """Modifies the given attribute of the player character by modifier. By default
        this is achieved via addition, but prepending a '%' will cause it to be 
        multiplied by the attribute.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: attribute, modifier
        
        Action parameter 'modifier' must be an int (positive or negative)
        **Example:**

        >>> action.__dict__
        {
            "type": "change_player_attribute",
            "parameters": [
                "walkrate",
                "1.50"
            ]
        }
        """
        world = game.get_state_name("WorldState")
        if not world:
            return

        attribute = action.parameters[0]
        modifier = action.parameters[1]
        
        Common.modify_character_attribute(world.player1, attribute, modifier)

    def remove_monster(self, game, action, contexts):
        """Removes a monster to the current player's party if the monster is there.

        :param game: The main game object that contains all the game's variables.
        :param action: The action (tuple) retrieved from the database that contains the action's
            parameters

        :type game: core.control.Control
        :type action: Tuple

        :rtype: None
        :returns: None

        Valid Parameters: monster_slug
        """
        monster_slug = action.parameters[0]

        monster = game.player1.find_monster(monster_slug)
        if monster:
            game.player1.remove_monster(monster)
