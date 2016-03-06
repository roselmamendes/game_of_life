import unittest

from game_of_life import CellState, Board


class GameOfLifeTest(unittest.TestCase):
    def test_create_board(self):
        board = Board([
            [0, 0, 0],
            [1, 0, 1],
            [0, 0, 0]
        ])

        self.assertEqual(board.cell_at(0, 1), CellState.alive)
        self.assertEqual(board.cell_at(1, 1), CellState.dead)

    def test_number_of_alive_neighbours(self):
        board = Board([
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ])

        self.assertEqual(board.num_alive_neighbours(1, 1), 3)
        self.assertEqual(board.num_alive_neighbours(2, 1), 1)

    def test_an_alive_cell_without_living_neighbours_dies(self):
        board = Board([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])

        board.evolve()

        self.assertEqual(board.cell_at(1, 1), CellState.dead)

    def test_an_alive_cell_with_four_neighbours_dies(self):
        board = Board([
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0]
        ])

        board.evolve()

        self.assertEqual(board.cell_at(1, 1), CellState.dead)

    def test_an_alive_cell_with_one_neighbours_dies(self):
        board = Board([
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ])

        board.evolve()

        self.assertEqual(board.cell_at(1, 1), CellState.dead)

    def test_an_alive_cell_with_more_than_four_neighbours_dies(self):
        board = Board([
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 0]
        ])

        board.evolve()

        self.assertEqual(board.cell_at(1, 1), CellState.dead)

    def test_a_dead_cell_with_three_alive_neighbours_resurrects(self):
        board = Board([
            [0, 1],
            [1, 1]
        ])

        board.evolve()

        self.assertEqual(board.cell_at(0, 0), CellState.alive)
