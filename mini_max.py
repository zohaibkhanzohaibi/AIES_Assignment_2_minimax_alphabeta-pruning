import random

# Board
board = [['' for _ in range(3)] for _ in range(3)]

ai = 'X'
human = 'O'
currentPlayer = human

# Counters for minimax checks
total_checks = 0
current_checks = 0

def print_board():
    print("\nCurrent Board:")
    for row in board:
        print('| ' + ' | '.join([cell if cell != '' else ' ' for cell in row]) + ' |')

def equals3(a, b, c):
    return a == b == c and a != ''

def check_winner():
    winner = None

    # Horizontal
    for i in range(3):
        if equals3(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]

    # Vertical
    for i in range(3):
        if equals3(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]

    # Diagonal
    if equals3(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]
    if equals3(board[2][0], board[1][1], board[0][2]):
        winner = board[2][0]

    open_spots = sum(cell == '' for row in board for cell in row)

    if winner is None and open_spots == 0:
        return 'tie'
    else:
        return winner

def available_moves():
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                moves.append((i, j))
    return moves

def minimax(new_board, depth, is_maximizing):
    global current_checks, total_checks
    current_checks += 1
    total_checks += 1

    result = check_winner()
    if result is not None:
        if result == ai:
            return 1
        elif result == human:
            return -1
        elif result == 'tie':
            return 0

    if is_maximizing:
        best_score = -float('inf')
        for (i, j) in available_moves():
            new_board[i][j] = ai
            score = minimax(new_board, depth + 1, False)
            new_board[i][j] = ''
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (i, j) in available_moves():
            new_board[i][j] = human
            score = minimax(new_board, depth + 1, True)
            new_board[i][j] = ''
            best_score = min(score, best_score)
        return best_score

def best_move():
    global current_checks
    best_score = -float('inf')
    move = None
    current_checks = 0  # Reset for this move
    for (i, j) in available_moves():
        board[i][j] = ai
        score = minimax(board, 0, False)
        board[i][j] = ''
        if score > best_score:
            best_score = score
            move = (i, j)
    if move:
        i, j = move
        board[i][j] = ai

    print(f"AI evaluated {current_checks} positions for its move.")

def main():
    global currentPlayer, total_checks

    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        winner = check_winner()
        if winner is not None:
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            print(f"Total minimax evaluations during the game: {total_checks}")
            break

        if currentPlayer == human:
            try:
                move = input("Enter your move (row and column: 0 0 for top-left): ")
                i, j = map(int, move.split())
                if board[i][j] == '':
                    board[i][j] = human
                    currentPlayer = ai
                else:
                    print("Invalid move, spot already taken.")
            except:
                print("Invalid input. Please enter row and column separated by space.")
        else:
            print("AI's Turn...")
            best_move()
            currentPlayer = human

        print_board()

if __name__ == "__main__":
    main()
