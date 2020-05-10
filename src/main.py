from src.model.game import Game
import pygame as pg


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption("Game Of Life")

    zygote = read_file("../zygotes/2")
    Game(zygote).run()
