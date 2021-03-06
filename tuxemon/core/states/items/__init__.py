from __future__ import division

from core import tools
from core.components.locale import translator
from core.components.menu.interface import MenuItem
from core.components.menu.menu import Menu
from core.components.sprite import Sprite
from core.components.ui.text import TextArea
from core.components.game_event import *

trans = translator.translate


class ItemMenuState(Menu):
    """ The item menu allows you to view and use items in your inventory.
    """
    background_filename = "gfx/ui/item/item_menu_bg.png"
    draw_borders = False

    def startup(self, **kwargs):
        self.state = "normal"

        # this sprite is used to display the item
        # its also animated to pop out of the backpack
        self.item_center = self.rect.width * .164, self.rect.height * .13
        self.item_sprite = Sprite()
        self.item_sprite.image = None
        self.sprites.add(self.item_sprite)

        # do not move this line
        super(ItemMenuState, self).startup(**kwargs)
        self.menu_items.line_spacing = tools.scale(5)

        # this is the area where the item description is displayed
        rect = self.game.screen.get_rect()
        rect.top = tools.scale(106)
        rect.left = tools.scale(3)
        rect.width = tools.scale(250)
        rect.height = tools.scale(32)
        self.text_area = TextArea(self.font, self.font_color, (96, 96, 128))
        self.text_area.rect = rect
        self.sprites.add(self.text_area, layer=100)

        # load the backpack icon
        self.backpack_center = self.rect.width * .16, self.rect.height * .45
        self.load_sprite("gfx/ui/item/backpack.png", center=self.backpack_center, layer=100)

        #print("item menu length: ")
        #print(len(self.menu_items))

    def process_event_hook(self, event):
        print(len(self.menu_items))
        if (event.type == MENU_EVENT and "items_menu" in event.target_menu):
            print("inside items menu handler")
            print(len(self.menu_items))
            for i in range(0, len(self.menu_items)):
                print("Item name: " + self.menu_items[i].game_object.name)

                if (event.item_name in self.menu_items[i].game_object.name):
                    print("Using " + event.item_name)
                    self.change_selection(i)
                    self.on_menu_selection(self.get_selected_item())
                    break

    def calc_internal_rect(self):
        # area in the screen where the item list is
        rect = self.rect.copy()
        rect.width *= .58
        rect.left = self.rect.width * .365
        rect.top = rect.height * .05
        rect.height = self.rect.height * .60
        return rect

    def determine_state_called_from(self):
        dex = self.game.active_states.index(self)
        return self.game.active_states[dex + 1].name

    def on_menu_selection(self, menu_item):
        """ Called when player has selected something from the inventory

        Currently, opens a new menu depending on the state context

        :param menu_item:
        :return:
        """
        item = menu_item.game_object
        state = self.determine_state_called_from()

        if state in item.usable_in:
            self.open_confirm_use_menu(item)
        else:
            msg = trans('item_cannot_use_here', {'name': item.name})
            tools.open_dialog(self.game, [msg])

    def open_confirm_use_menu(self, item):
        """ Confirm if player wants to use this item, or not

        :return: None
        """
        def use_item(menu_item):
            player = self.game.player1
            monster = menu_item.game_object

            # item must be used before state is popped.
            # don't try to combine with "if result..." condition below
            result = item.use(player, monster)
            self.game.pop_state()    # pop the monster screen
            self.game.pop_state()    # pop the item screen
            if result["success"]:
                tools.open_dialog(self.game, [trans('item_success')])
            else:
                tools.open_dialog(self.game, [trans('item_failure')])

        def confirm():
            self.game.pop_state()  # close the confirm dialog
            # TODO: allow items to be used on player or "in general"

            menu = self.game.push_state("MonsterMenuState")
            menu.on_menu_selection = use_item

        def cancel():
            self.game.pop_state()  # close the use/cancel menu

        def open_choice_menu():
            # open the menu for use/cancel
            menu = self.game.push_state("Menu")
            menu.shrink_to_items = True

            menu_items_map = (
                ('item_confirm_use', confirm),
                ('item_confirm_cancel', cancel)
            )

            # add our options to the menu
            for key, callback in menu_items_map:
                label = translator.translate(key).upper()
                image = self.shadow_text(label)
                item = MenuItem(image, label, None, callback)
                menu.add(item)

        open_choice_menu()

    def initialize_items(self):
        """ Get all player inventory items and add them to menu

        :return:
        """
        for name, properties in self.game.player1.inventory.items():
            obj = properties['item']
            quantity = properties['quantity']

            # temporarily add the quantity to the name
            old_name = obj.name
            obj.name += " x " + str(quantity)

            image = self.shadow_text(obj.name, bg=(128, 128, 128))
            yield MenuItem(image, obj.name, obj.description, obj)

            # restore the original name
            obj.name = old_name

    def on_menu_selection_change(self):
        """ Called when menu selection changes

        :return: None
        """
        item = self.get_selected_item()
        if item:
            # animate item being pulled from the bag
            image = item.game_object.surface
            self.item_sprite.image = image
            self.item_sprite.rect = image.get_rect(center=self.backpack_center)
            self.animate(self.item_sprite.rect, centery=self.item_center[1], duration=.2)

            # show item description
            self.alert(item.description)
