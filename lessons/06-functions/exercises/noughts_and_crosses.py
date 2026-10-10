def print_board(board):
    """Prints the board"""
    ...


def get_move(board, player):
    """Asks `player` for a row and column until they choose an empty square"""
    ...
    return row, col


def has_won(board, player):
    """Returns `True` if `player` has three in a row"""
    ...


# Create an empty board. Each square is either " " (empty), "X" or "O".
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

player = "X"
for turn in range(9):
    print_board(board)
    row, col = get_move(board, player)
    board[row][col] = player

    if has_won(board, player):
        ...

    # Swap players
    ...
