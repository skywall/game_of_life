from enum import Enum, unique

import pygame as pg


@unique
class MenuAction(Enum):
    NEXT = "next",
    PLUS = "plus",
    MINUS = "minus",
    CLEAR = "clear",


class Menu:
    loaded_images = {
        "active": {},
        "focused": {}
    }

    menu_items_rects = []

    def __init__(self):
        current_width = 0

        # noinspection PyTypeChecker
        for item in list(MenuAction):
            loaded_item_active = pg.image.load("../img/" + item.name + "_active.png")
            loaded_item_focused = pg.image.load("../img/" + item.name + "_focused.png")

            # cache items
            self.loaded_images["active"][item.name] = loaded_item_active
            self.loaded_images["focused"][item.name] = loaded_item_focused

            # compute next menu item rect left position
            rect = loaded_item_active.get_rect()
            rect.left += current_width
            current_width += rect.width

            self.menu_items_rects.append((rect, item))

    def draw(self, surface, mouse_pos):
        for (rect, action) in self.menu_items_rects:
            if mouse_pos != (0, 0) and rect.collidepoint(mouse_pos):
                next_item = self.loaded_images["focused"][action.name]
            else:
                next_item = self.loaded_images["active"][action.name]

            surface.blit(next_item, rect)

    def handle_click(self, pos) -> MenuAction:
        for (rect, action) in self.menu_items_rects:
            if rect.collidepoint(pos):
                return action
