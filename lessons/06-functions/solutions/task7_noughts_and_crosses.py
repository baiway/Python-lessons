def print_board(board):
    """Prints the board"""
    for row in board:
        print(" | ".join(row))


def get_move(board, player):
    """Asks `player` for a row and column until they choose an empty square"""
    print(f"Player {player}'s turn.")
    while True:
        row = int(input("Row (0-2): "))
        col = int(input("Column (0-2): "))
        if board[row][col] == " ":
            return row, col
        print("That square is already taken! Try again.")


def has_won(board, player):
    """Returns `True` if `player` has three in a row"""
    # Check the rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check the two diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# Create an empty board. Each square is either " " (empty), "X" or "O".
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

player = "X"
winner = None  # `None` means "no winner yet"
for turn in range(9):
    print_board(board)
    row, col = get_move(board, player)
    board[row][col] = player

    if has_won(board, player):
        winner = player
        break

    # Swap players
    if player == "X":
        player = "O"
    else:
        player = "X"

# Print the final board and the result
print_board(board)
if winner is None:
    print("The board is full. It's a draw!")
else:
    print(f"Player {winner} wins!")
