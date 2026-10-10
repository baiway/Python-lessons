# Create an empty board. Each square is either " " (empty), "X" or "O".
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

player = "X"
num_moves = 0

while num_moves < 9:
    # Print the board
    for row in board:
        print(" | ".join(row))  # puts " | " between each square in the row

    # Ask the current player for a row and column
    print(f"Player {player}'s turn.")
    row = int(input("Row (0-2): "))
    col = int(input("Column (0-2): "))

    # Check whether the square is free. If it is, place the player's symbol
    # there, otherwise tell them to try again
    if board[row][col] == " ":
        board[row][col] = player
        num_moves = num_moves + 1

        # Swap players
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("That square is already taken! Try again.")

print("The board is full. It's a draw!")
