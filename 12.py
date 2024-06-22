def print_board(board):
    for row in board:
        print(" ".join(row))
def check_winner(board, player):
    win_cond = [player] * 3
    return any(
        row == win_cond or
        col == win_cond or
        [board[i][i] for i in range(3)] == win_cond or
        [board[i][2 - i] for i in range(3)] == win_cond
        for row in board for col in zip(*board)
    )
def get_move():
    return map(int, input("Enter row and column (0, 1, 2): ").split())
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    for turn in range(9):
        print_board(board)
        player = players[turn % 2]
        row, col = get_move()
        while board[row][col] != " ":
            print("Cell already taken. Try again.")
            row, col = get_move()
        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
    print_board(board)
    print("It's a tie!")
tic_tac_toe()
