num_moves = 0


def hanoi(n, source, target, spare):
    """Prints the moves needed to move `n` discs from `source` to `target`"""
    global num_moves
    if n == 0:
        return  # nothing to move!

    hanoi(n - 1, source, spare, target)  # move the smaller discs out of the way
    print(f"Move disc {n} from {source} to {target}")
    num_moves = num_moves + 1
    hanoi(n - 1, spare, target, source)  # move them back on top


for n in [3, 4, 5]:
    num_moves = 0
    print(f"--- {n} discs ---")
    hanoi(n, "A", "C", "B")
    print(f"{n} discs took {num_moves} moves")

# 3 discs take 7 moves, 4 take 15, and 5 take 31. Each extra disc doubles the
# number of moves (plus one), so n discs take 2^n - 1 moves. Legend has it that
# monks are solving a 64-disc version: that would take 2^64 - 1 moves, which,
# at one move per second, would take about 585 billion years!
