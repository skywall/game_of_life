from src.model.cell import Health


def next_gen_health(cell, alive_neighbors_count):
    if cell.health == Health.ALIVE:
        if alive_neighbors_count in range(2, 4):
            return Health.ALIVE
    else:
        if alive_neighbors_count == 3:
            return Health.ALIVE

    return Health.DEAD
