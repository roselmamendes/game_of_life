from enum import IntEnum
import itertools as it

class CellState(IntEnum):
    is_alive = 1
    is_dead = 0


class Board:
    def __init__(self, cells):
        self.cells = cells

    def cell_at(self, x, y):
        if x < 0 or y < 0:
            return CellState.is_dead

        try:
            return CellState(self.cells[y][x])
        except IndexError:
            return CellState.is_dead

    def num_alive_neighbours(self, x, y):
        neighbours = it.product(range(-1, 2), range(-1, 2))

        return sum([self.cell_at(relX + x, relY + y) for (relX, relY) in neighbours if not relX == relY == 0])

    def evolve(self):
        width = len(self.cells[0])
        height = len(self.cells)

        must_kill = []
        lazaruses = []

        for x in range(width):
            for y in range(height):
                living_neighbors = self.num_alive_neighbours(x, y)

                if not 1 < living_neighbors < 4:
                    must_kill.append((x, y))

                if living_neighbors == 3 and self.cell_at(x, y) == CellState.is_dead:
                    lazaruses.append((x, y))

        self.kill_all(must_kill)
        self.resurrect(lazaruses)

    def kill(self, x, y):
        self.cells[y][x] = CellState.is_dead

    def kill_all(self, must_kill):
        for (x, y) in must_kill:
            self.kill(x, y)

    def resurrect(self, lazaruses):
        for (x, y) in lazaruses:
            self.cells[y][x] = CellState.is_alive

    def __str__(self):
        def printable(c):
            if c == CellState.is_alive:
                return '*'
            else:
                return ' '

        lines = ("".join(printable(c) for c in line) for line in self.cells)
        return "\n".join(lines)
