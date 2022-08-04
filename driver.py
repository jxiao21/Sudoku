import copy

from tabnanny import check
import board as b
import sudoku_solver as ss

if __name__ == '__main__':
    print('Welcome to Sudoku!')

    board = b.create_board()
    is_valid = ss.solve_sudoku(board)

    # if board is not valid, generate a new one
    while is_valid == False:
        print()
        board = b.create_board()
        is_valid = ss.solve_sudoku(board)
    print()

    solution = copy.deepcopy(board)

    for i in range(60):
        zero_to_eight = list(range(0, 9))
        row = b.random.choice(zero_to_eight)
        col = b.random.choice(zero_to_eight)
        board[row][col] = -1
    
    curr_board = copy.deepcopy(board)
    print()

    while sorted(solution) != sorted(curr_board):
        print()
        ss.print_board(curr_board)
        print()

        check_sol = input('Do you want to see the solution? WARNING: LOOKING AT THE SOLUTION \nWILL END THE GAME! [Y/N]: ')
        while check_sol != 'N' and check_sol != 'Y':
            print('Invalid input. Please enter "Y" or "N".')
            check_sol = input('Do you want to see the solution? WARNING: LOOKING AT THE SOLUTION \nWILL END THE GAME![Y/N]: ')

        if check_sol == 'Y':
            print()
            print('Better luck next time!')
            break

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        guess_col = input('Enter a column letter: ')
        while guess_col not in letters:
            print()
            guess_col = input('Invalid input. Please enter a column letter A-I: ')
        
        guess_row = input('Enter a row number: ')
        while guess_row not in nums:
            print()
            guess_col = input('Invalid input. Please enter a row number 1-9: ')
        
        if board[nums.index(guess_row)][letters.index(guess_col)] != -1:
            print('That spot has already been provided to you.')
            continue

        input_num = input('Enter a number to fill in: ')
        while input_num not in nums:
            print()
            print(type(input_num))
            input_num = input('Invalid number. Please enter a number 1-9: ')
        
        curr_board[nums.index(guess_row)][letters.index(guess_col)] = int(input_num)

    print()
    ss.print_board(solution)
    print()
    print('Thanks for playing Sudoku!')
    print()