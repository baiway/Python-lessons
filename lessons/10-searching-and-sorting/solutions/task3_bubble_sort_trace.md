# Task 3 solution
| Pass | Comparisons                                         | List after pass   |
|------|-----------------------------------------------------|-------------------|
| 1    | 6 > 2, swap. 6 < 9, no swap. 9 > 4, swap. 9 > 1, swap. | `[2, 6, 4, 1, 9]` |
| 2    | 2 < 6, no swap. 6 > 4, swap. 6 > 1, swap.           | `[2, 4, 1, 6, 9]` |
| 3    | 2 < 4, no swap. 4 > 1, swap.                        | `[2, 1, 4, 6, 9]` |
| 4    | 2 > 1, swap.                                        | `[1, 2, 4, 6, 9]` |
| 5    | No swaps, so the list is sorted!                    | `[1, 2, 4, 6, 9]` |

It takes 5 passes. Notice that:
- After each pass, one more item at the end of the list is in its final position (`9` after pass 1, `6` after pass 2, and so on). This means each pass can make one fewer comparison than the one before.
- The `1` only moves one place to the left in each pass. Small items near the end of the list are slow to reach the front, which is why this list needed so many passes.
- Even though the list was sorted after pass 4, the algorithm can't know that until it has made a pass with no swaps.
