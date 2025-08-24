def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*5)
def check_winner(board,player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
        return False
def is_full(board):
    return all(cell != "" for row in board for cell in row)
def tic_tac_toe():
    board = [["" for _ in range(3)]for _ in range(3)]
    players = ["x","o"]
    turn = 0
    while True:
        print_board(board)
        player = players[turn%2]
        print(f"player{player}'s turn")
        try:
            row = int(input("Enter row(0-2)"))
            col = int(input("Enter col(0-2)"))
        except ValueError:
            print("Invalid input please enter the number")
            continue
        if row not in range(3) or col not in range(3) or board[row][col]!= "":
            print("Invalid move try again")
            continue
        board[row][col] = player
        if check_winner(board,player):
            print_board(board)
            print(f"congratulation{player}wins")
            break
        if is_full(board):
            print_board(board)
            print("Is a draw")
            break
        turn += 1
tic_tac_toe()