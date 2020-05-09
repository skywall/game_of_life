from enum import Enum


class Health(Enum):
    ALIVE = "*"
    DEAD = "."

    def __str__(self):
        return self.value


class Cell:

    def __init__(self, health: Health):
        self.health = health

    def __repr__(self):
        return str(self.health)

    def value(self):
        return int(self.health == Health.ALIVE)
