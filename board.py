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

if __name__ == '__main__':
    board = create_board()
    solution = copy.deepcopy(board)

    #while solution == False:
     #   board = create_board()
      #  solution = copy.deepcopy(board)

    # if board == solution:
    #     print('Equal')
    # else:
    #     print('not equal')

    # solution = ss.solve_sudoku(solution)
    # print(solution)
    # if board == solution:
    #     print('Equal')
    # else:
    #     print('not equal')

    # ss.solve_sudoku(board)
    # if board == solution:
    #     print('Equal')
    # else:
    #     print('not equal')

    # print()
    # if sorted(board[0]) == sorted(solution[0]) or\
    #    sorted(board[1]) == sorted(solution[1]) or\
    #    sorted(board[2]) == sorted(solution[2]) or\
    #    sorted(board[3]) == sorted(solution[3]) or\
    #    sorted(board[4]) == sorted(solution[4]) or\
    #    sorted(board[5]) == sorted(solution[5]) or\
    #    sorted(board[6]) == sorted(solution[6]) or\
    #    sorted(board[7]) == sorted(solution[7]) or\
    #    sorted(board[8]) == sorted(solution[8]):
    #     print('Equal')
    # else:
    #     print('not equal!')

    print (sorted(board) == sorted(solution))
    print()

    ss.solve_sudoku(board)
    print (sorted(board) == sorted(solution))
    print()

    ss.solve_sudoku(solution)
    print (sorted(board) == sorted(solution))