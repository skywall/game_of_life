import numpy as np

from src import rules
from src.model.cell import Cell, Health


class Board:
    rows = 0
    cols = 0
    matrix = np.empty((0,0))

    def __init__(self, rows=20, cols=20):
        self.set_board_size(rows, cols)

    def __str__(self):
        return str(self.matrix)

    def load(self, data):
        rows = len(data)
        cols = len(data[0])

        if rows > self.rows or cols > self.cols:
            self.set_board_size(rows, cols)

        # noinspection PyTypeChecker
        self.matrix.fill(Cell(Health.DEAD))

        for x, row in enumerate(data):
            for y, item in enumerate(row):
                if item == "\n":
                    continue

                self.matrix[x, y] = Cell(Health(item))

    def next_gen(self):
        # noinspection PyTypeChecker
        new_matrix = np.full((self.rows, self.cols), Cell(Health.DEAD), dtype=Cell)

        for x in range(self.rows):
            for y in range(self.cols):
                alive_neighbors_count = self.__get_alive_neighbors_count(x, y)
                next_gen_health = rules.next_gen_health(self.matrix[x, y], alive_neighbors_count)
                new_matrix[x, y] = Cell(next_gen_health)

        self.matrix = new_matrix

    def set_board_size(self, rows, cols):
        # noinspection PyTypeChecker
        self.matrix = np.full((rows, cols), Cell(Health.DEAD), dtype=Cell)

        self.rows = rows
        self.cols = cols

    def __get_alive_neighbors_count(self, x, y):
        count = 0
        for x_n in range(max(0, x - 1), min(x + 1 + 1, self.rows)):
            for y_n in range(max(0, y - 1), min(y + 1 + 1, self.cols)):
                if x_n == x and y_n == y:
                    continue

                count += self.matrix[x_n, y_n].value()

        return count
