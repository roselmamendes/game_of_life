import time
from game_of_life import Board
import os

board = Board([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
])

for i in range(100):
    print(board)
    board.evolve()
    time.sleep(1)
    os.system('clear')
