import pygame as pg

from src.menu import Menu, MenuAction
from src.model.board import Board


class Game:
    menu = Menu()
    board = Board()

    grid_size_px = 20
    menu_height_px = 30

    def __init__(self, zygote):
        self.zygote = zygote
        self.board.load(self.zygote)
        self.__recompute_screens()

    def process_menu_action(self, pos):
        action = self.menu.handle_click(pos)

        if action == MenuAction.NEXT:
            self.board.next_gen()
        elif action == MenuAction.PLUS:
            self.board.increase_size()
            self.__recompute_screens()
        elif action == MenuAction.MINUS:
            self.board.decrease_size()
            self.__recompute_screens()
        elif action == MenuAction.CLEAR:
            self.board.clear()

    def run(self):
        done = False

        while not done:
            self.menu.draw(self.full_screen, pg.mouse.get_pos())
            self.board.draw(self.board_screen, self.grid_size_px)
            pg.display.update()

            e = pg.event.wait()
            if e.type == pg.QUIT:
                done = True
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                self.board.next_gen()
            if e.type == pg.MOUSEBUTTONUP:
                if e.pos[1] < self.menu_height_px:  # handle menu click
                    self.process_menu_action(e.pos)
                else:  # handle board click
                    self.board.handle_click((e.pos[0], e.pos[1] - self.menu_height_px), self.grid_size_px)

    def __recompute_screens(self):
        rows_px = self.board.rows * self.grid_size_px
        cols_px = self.board.cols * self.grid_size_px

        self.full_screen = pg.display.set_mode((cols_px, rows_px + self.menu_height_px))
        self.full_screen.fill((220, 220, 220))
        self.board_screen = self.full_screen.subsurface(pg.Rect(0, self.menu_height_px, cols_px, rows_px))
