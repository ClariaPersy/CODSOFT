import random

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the current player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to evaluate the current state of the board
def evaluate_board(board):
    if check_winner(board, 'X'):
        return -1  # Human player wins
    elif check_winner(board, 'O'):
        return 1   # AI player wins
    elif is_board_full(board):
        return 0   # It's a draw
    else:
        return None  # Game is still ongoing

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    score = evaluate_board(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '

                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)

                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '

                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)

                    if beta <= alpha:
                        break
        return min_eval

# Function to make AI move using Minimax with Alpha-Beta Pruning
def ai_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Main function to run the Tic-Tac-Toe game
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        display_board(board)

        if current_player == 'X':
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                current_player = 'O'
            else:
                print("Cell already taken. Try again.")
        else:
            print("AI is making a move...")
            move = ai_move(board)
            board[move[0]][move[1]] = 'O'
            current_player = 'X'

        result = evaluate_board(board)
        if result is not None:
            display_board(board)
            if result == -1:
                print("Human player wins!")
            elif result == 1:
                print("AI player wins!")
            else:
                print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
