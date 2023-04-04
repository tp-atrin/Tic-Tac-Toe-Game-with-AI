import random

# define the board as a list of 9 strings, with empty spaces represented by '-'
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


# print the board to the console
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()


# check if a player has won the game
def check_win(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))


# check if the board is full
def check_full(board):
    return '-' not in board


# define the minimax algorithm for determining the best move for the computer player
def minimax(board, depth, maximizing_player):
    if check_win(board, 'O'):
        return {'score': 10 - depth}
    elif check_win(board, 'X'):
        return {'score': depth - 10}
    elif check_full(board):
        return {'score': 0}

    if maximizing_player:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)['score']
                board[i] = '-'
                if score > best_score:
                    best_score = score
                    best_move = i
        return {'score': best_score, 'move': best_move}
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)['score']
                board[i] = '-'
                if score < best_score:
                    best_score = score
                    best_move = i
        return {'score': best_score, 'move': best_move}


# if it's the player's turn, get their move and update the board
# define the main game loop
def play_game():
    # randomly choose who goes first
    if random.choice([True, False]):
        player = 'X'
        print("You are X, you go first.")
    else:
        player = 'O'
        print("You are O, the computer goes first.")

    while True:
        print_board(board)

        # check if the game is over
        if check_win(board, 'X'):
            print("You win!")
            break
        elif check_win(board, 'O'):
            print("You lose!")
            break
        elif check_full(board):
            print("It's a tie!")
            break

        # if it's the player's turn, get their move and update the board
        if player == 'X':
            while True:
                move = input("Enter a number between 1 and 9: ")
                if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == '-':
                    board[int(move) - 1] = 'X'
                    player = 'O'
                    break
                else:
                    print("Invalid move, try again.")
        # if it's the computer's turn, use the minimax algorithm to determine the best move
        else:
            print("Thinking...")
            move = minimax(board, 0, True)['move']
            board[move] = 'O'
            player = 'X'


play_game()