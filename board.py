import random
import copy

from matplotlib.pyplot import fill
import sudoku_solver as ss

def create_board():
    starting_board = [
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1]
    ]

    # randomly fill some values in
    for i in range(1, 4):
        l = list(range(1, 10))
        one_to_three = [1, 2, 3]
        filler = random.choice(l)
        for j in range(10):
            row = random.choice(one_to_three) * i
            col = random.choice(one_to_three) * i
            while not ss.is_valid_guess(starting_board, filler, row - 1, col - 1):
                filler = random.choice(l)
            starting_board[row - 1][col - 1] = filler
        l.remove(filler)

    return starting_board