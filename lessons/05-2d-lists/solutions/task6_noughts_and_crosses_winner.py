# Create an empty board. Each square is either " " (empty), "X" or "O".
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

player = "X"
num_moves = 0
winner = None  # `None` means "no winner yet"

while num_moves < 9 and winner is None:
    # Print the board
    for row in board:
        print(" | ".join(row))  # puts " | " between each square in the row

    # Ask the current player for a row and column
    print(f"Player {player}'s turn.")
    row = int(input("Row (0-2): "))
    col = int(input("Column (0-2): "))

    # If the square is taken, skip back to the start of the loop
    if board[row][col] != " ":
        print("That square is already taken! Try again.")
        continue

    board[row][col] = player
    num_moves = num_moves + 1

    # Check the rows and columns. `i` is used as both a row and a column index.
    # Note that Python lets us chain `==` comparisons together: `a == b == c`
    # means `a == b and b == c`.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            winner = player
        if board[0][i] == board[1][i] == board[2][i] == player:
            winner = player

    # Check the two diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        winner = player
    if board[0][2] == board[1][1] == board[2][0] == player:
        winner = player

    # Swap players
    if player == "X":
        player = "O"
    else:
        player = "X"

# Print the final board and the result
for row in board:
    print(" | ".join(row))

if winner is None:
    print("The board is full. It's a draw!")
else:
    print(f"Player {winner} wins!")
