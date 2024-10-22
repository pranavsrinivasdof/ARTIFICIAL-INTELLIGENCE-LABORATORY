import random

board = [['', '', ''], ['', '', ''], ['', '', '']]

def print_board():
    for row in board:
        print(" | ".join(cell if cell != '' else ' ' for cell in row))
        print("-" * 9)

def start():
    print("Welcome to Tic-Tac-Toe!")
    random_num = random.randint(0, 1)
    if random_num == 0:
        print("Player plays first.")
    else:
        print("Computer plays first.")
        computer_plays()

    while True:
        if random_num == 0:
            player_plays()
            if check_win('X'):
                print_board()
                print("Player won!")
                return
            random_num = 1
        else:
            computer_plays()
            if check_win('O'):
                print_board()
                print("Computer won!")
                return
            random_num = 0

        if board_full():
            print_board()
            print("Draw!")
            return

def check_win(player):
    wins = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
   
    for win in wins:
        if all(board[x][y] == player for x, y in win):
            return True
    return False

def player_plays():
    print_board()
    while True:
        try:
            a, b = map(int, input("Enter the coordinates (row and column 0-2, e.g., '0 1'): ").split())
            if board[a][b] == '':
                board[a][b] = 'X'
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter coordinates in the format 'row column'.")

def computer_plays():
    _, move = minimax(board, 'O')
    board[move[0]][move[1]] = 'O'

def minimax(board, current_player):
    if check_win('X'):
        return -1, None
    elif check_win('O'):
        return 1, None
    elif board_full():
        return 0, None

    if current_player == 'O':
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score, _ = minimax(board, 'X')
                    board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score, _ = minimax(board, 'O')
                    board[i][j] = ''
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move

def board_full():
    return all(cell != '' for row in board for cell in row)

# Start the game
start()