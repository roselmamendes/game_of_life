from enum import IntEnum
import itertools as it


class CellState(IntEnum):
    alive = 1
    dead = 0


class Board:
    def __init__(self, cells):
        self.cells = cells

    def evolve(self):
        width = len(self.cells[0])
        height = len(self.cells)

        must_kill = []
        lazaruses = []

        for x in range(width):
            for y in range(height):
                self.check_cell(lazaruses, must_kill, x, y)

        self.kill_all(must_kill)
        self.resurrect_all(lazaruses)

    def check_cell(self, lazaruses, must_kill, x, y):
        living_neighbours = self.num_alive_neighbours(x, y)
        if self.cell_on_under_population(living_neighbours):
            must_kill.append((x, y))
        if self.cell_on_over_population(living_neighbours, self.cell_at(x, y)):
            lazaruses.append((x, y))

    def num_alive_neighbours(self, x, y):
        neighbours = it.product(range(-1, 2), range(-1, 2))

        return sum([self.cell_at(relX + x, relY + y) for (relX, relY) in neighbours if not relX == relY == 0])

    def cell_on_under_population(self, living_neighbours):
        return not 1 < living_neighbours < 4

    def cell_on_over_population(self, living_neighbours, cell):
        return living_neighbours == 3 and cell == CellState.dead

    def kill_all(self, must_kill):
        for (x, y) in must_kill:
            self.kill(x, y)

    def kill(self, x, y):
        self.cells[y][x] = CellState.dead

    def resurrect_all(self, lazaruses):
        for (x, y) in lazaruses:
            self.ressurect(x, y)

    def ressurect(self, x, y):
        self.cells[y][x] = CellState.alive

    def cell_at(self, x, y):
        if x < 0 or y < 0:
            return CellState.dead

        try:
            return CellState(self.cells[y][x])
        except IndexError:
            return CellState.dead

    def __str__(self):
        def printable(c):
            if c == CellState.alive:
                return '*'
            else:
                return ' '

        lines = ("".join(printable(c) for c in line) for line in self.cells)
        return "\n".join(lines)
