import random

def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n---------")

def check_win(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def make_random_move(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                available_moves.append((i, j))
    row, col = random.choice(available_moves)
    return row, col

def play_tic_tac_toe():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    current_player = 'X'
    winner = None

    while winner is None and not is_board_full(board):
        print_board(board)
        
        if current_player == 'X':
            print(f"Player {current_player}'s turn.")
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
        else:
            print(f"Computer's turn (Player {current_player}).")
            row, col = make_random_move(board)

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_win(board)

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print("Invalid move. Try again.")

    print_board(board)

    if winner:
        if winner == 'X':
            winner_name = 'Player X'
        else:
            winner_name = 'Player O'
        print(f"{winner_name} wins!")
    else:
        print("It's a tie!")

play_tic_tac_toe()
