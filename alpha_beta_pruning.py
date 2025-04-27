import random

# Board setup
board = [['' for _ in range(3)] for _ in range(3)]
ai, human = 'X', 'O'
currentPlayer = human

# Counters for minimax evaluations
total_checks = 0
current_checks = 0

def print_board():
    print("\nCurrent Board:")
    for row in board:
        print('| ' + ' | '.join([cell if cell else ' ' for cell in row]) + ' |')

def equals3(a, b, c):
    return a == b == c and a != ''

def check_winner():
    for i in range(3):
        if equals3(board[i][0], board[i][1], board[i][2]): return board[i][0]
        if equals3(board[0][i], board[1][i], board[2][i]): return board[0][i]
    if equals3(board[0][0], board[1][1], board[2][2]): return board[0][0]
    if equals3(board[2][0], board[1][1], board[0][2]): return board[2][0]
    if all(cell != '' for row in board for cell in row): return 'tie'
    return None

def available_moves():
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']

def minimax(depth, is_maximizing, alpha, beta):
    global current_checks, total_checks
    current_checks += 1
    total_checks += 1

    result = check_winner()
    if result:
        return {'X': 1, 'O': -1, 'tie': 0}[result]

    if is_maximizing:
        best_score = -float('inf')
        for (i, j) in available_moves():
            board[i][j] = ai
            score = minimax(depth + 1, False, alpha, beta)
            board[i][j] = ''
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for (i, j) in available_moves():
            board[i][j] = human
            score = minimax(depth + 1, True, alpha, beta)
            board[i][j] = ''
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def best_move():
    global current_checks
    move = None
    best_score = -float('inf')
    current_checks = 0  # Reset counter for this move
    for (i, j) in available_moves():
        board[i][j] = ai
        score = minimax(0, False, -float('inf'), float('inf'))
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
        if winner:
            print("\nGame Over!")
            print_board()
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            print(f"Total minimax(alpha-beta pruned) evaluations during the game: {total_checks}")
            break

        if currentPlayer == human:
            try:
                move = input("\nEnter your move (row col): ")
                i, j = map(int, move.split())
                if 0 <= i <= 2 and 0 <= j <= 2 and board[i][j] == '':
                    board[i][j] = human
                    currentPlayer = ai
                else:
                    print("Invalid move, spot taken or out of range.")
            except:
                print("Invalid input. Please enter row and column separated by a space.")
        else:
            print("\nAI's Turn...")
            best_move()
            currentPlayer = human

        print_board()

if __name__ == "__main__":
    main()
