import copy
import board as b
import sudoku_solver as ss

def play():
    board = b.create_board()
    is_valid = ss.solve_sudoku(board)

    # if board is not valid, generate a new one
    while is_valid == False:
        print()
        board = b.create_board()
        is_valid = ss.solve_sudoku(board)
    print()

    # store solved board in separate deep copy
    solution = copy.deepcopy(board)

    # remove random values from solved board
    # keeping board as is for the entire game so we know which values were
    # originally on the board
    for i in range(60):
        zero_to_eight = list(range(0, 9))
        row = b.random.choice(zero_to_eight)
        col = b.random.choice(zero_to_eight)
        board[row][col] = -1
    
    # store unsolved board in separate deep copy
    curr_board = copy.deepcopy(board)
    print()

    # sorted works since every list in solution should have exact same values and rows
    while sorted(solution) != sorted(curr_board):
        print()
        ss.print_board(curr_board)
        print()

        # store column and row values
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'board', 'end']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        # get user input and check for invalid inputs
        print('Please enter "BOARD" to see the original board OR')
        print('Enter "END" to see the solution OR')
        guess_col = input('Enter a column letter: ').lower()
        while guess_col not in letters:
            print()
            guess_col = input('Invalid input. Please enter a column letter A-I or "BOARD": ')
        
        if guess_col == 'board':
            print()
            print('ORIGINAL BOARD:')
            print()
            ss.print_board(board)
            print()
            print('     ', end='')
            print('=' * 49)
            print()
            continue

        # make sure they want to end game
        if guess_col == 'end':
            print()
            check_sol = input('Do you want to see the solution? WARNING: LOOKING AT THE SOLUTION \nWILL END THE GAME! [Y/N]: ').lower()
            while check_sol != 'n' and check_sol != 'y':
                print('Invalid input. Please enter "Y" or "N".')
                check_sol = input('Do you want to see the solution? WARNING: LOOKING AT THE SOLUTION \nWILL END THE GAME![Y/N]: ').lower()

            if check_sol == 'y':
                print()
                print('Better luck next time!')
                break
            else:
                print()
                continue
        
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
        
        # update curr_board which is separate from solution and board
        curr_board[nums.index(guess_row)][letters.index(guess_col)] = int(input_num)
        if sorted(solution) == sorted(curr_board):
            print('Congrats! You win!')

    ss.print_board(solution)
    print()

if __name__ == '__main__':
    print('Welcome to Sudoku!')
    print()
    play_again = 'y'
    while play_again == 'y':
        play()
        play_again = input('Would you like to play again? [Y/N]: ').lower()
        while play_again != 'y' and play_again != 'n':
            print('Invalid input. Please enter "Y" or "N".')
            play_again = input('Would you like to play again? [Y/N]: ').lower()
    print('Thanks for playing Sudoku!')
    print()