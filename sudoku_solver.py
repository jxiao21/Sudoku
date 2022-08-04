import random

# Solve puzzle by backtracking
# Puzzle is list of lists that represents sudoku board
# If solution exists, mutate puzzle to be solution
# Else, return false
def solve_sudoku(puzzle):
    # Step 1 is choose somewhere on board to guess
    row, col = find_next_empty_square(puzzle)

    # Validate: If no empty spots left, we're done since there are no
    # valid inputs left and we have solved our puzzle
    if row is None:
        return True

    # Step 2: If there is a place to guess, guess a number between 1-9
    
    for guess in range(1, 10):
        # Step 3: Check if valid guess
        if is_valid_guess(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # Step 4: recursively continue 
            if solve_sudoku(puzzle):
                return True
    
        # Step 5: If not valid guess or guess does not solve puzzle, we
        # need to backtrack to try new number
        puzzle[row][col] = -1

    # Step 6: If none of the numbers work, this puzzle is unsolvable
    return False


# Find next row, col that's empty (equal to -1)
# Return None, None if there is none
def find_next_empty_square(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None


# Check if guess at row, col is a valid guess and returns 
# True/False accordingly
def is_valid_guess(puzzle, guess, row, col):
    # If guess is in the row, return False
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # If guess is in the col, return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # If guess is in 3x3 grid/square, return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if guess == puzzle[r][c]:
                return False

    # If it gets here, it must be valid
    return True


def print_board(puzzle):
    print('       A    B    C      D    E    F      G    H    I')
    print()

    row_count = 0
    for row in puzzle:
        col_count = 0
        if row_count % 3 == 0 and row_count != 0:
            print('     ', end='')
            print('-' * 49)
        print(row_count + 1, '   ', end='')
        for num in row:
            if col_count % 3 == 0 and col_count != 0:
                print('| ', end='')
            if num == -1:
                num = '_'
            print(' ', num, ' ', end='')
            col_count += 1
        print()
        row_count += 1


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    example_board_2 = [
        [4, 8, 1,   -1, -1, -1,   -1, -1, -1],
        [7, 9, 6,   3, -1, 1,   -1, -1, -1],
        [4, -1, 2,   -1, -1, -1,   -1, -1, 3],

        [-1, 1, -1,   4, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, 4,   6, -1, 8,   -1, -1, -1],

        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, 3,   -1, -1, 8]
    ]
    print(solve_sudoku(example_board_2))
    print(example_board_2)