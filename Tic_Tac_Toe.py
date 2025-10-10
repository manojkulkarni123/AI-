import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(f" {board[3*i]} | {board[3*i+1]} | {board[3*i+2]} ")
        if i < 2:
            print("---+---+---")
    print()

def is_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full():
    return ' ' not in board

def minimax(is_maximizing):
    if is_winner('O'):
        return 1
    elif is_winner('X'):
        return -1
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input! Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("That spot is already taken! Try again.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    print("Welcome to Tic Tac Toe! You are X, AI is O.")
    print_board()

    while True:
        player_move()
        print_board()
        if is_winner('X'):
            print("You win! Congrats!")
            break
        if is_board_full():
            print("It's a tie!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if is_winner('O'):
            print("AI wins! Better luck next time.")
            break
        if is_board_full():
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
