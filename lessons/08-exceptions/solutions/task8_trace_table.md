# Task 8 solution
| `n` | `n % 2 == 0` | `steps` | Output |
|-----|--------------|---------|--------|
| 6   |              | 0       |        |
|     | `True`       |         |        |
| 3   |              | 1       |        |
|     | `False`      |         |        |
| 10  |              | 2       |        |
|     | `True`       |         |        |
| 5   |              | 3       |        |
|     | `False`      |         |        |
| 16  |              | 4       |        |
|     | `True`       |         |        |
| 8   |              | 5       |        |
|     | `True`       |         |        |
| 4   |              | 6       |        |
|     | `True`       |         |        |
| 2   |              | 7       |        |
|     | `True`       |         |        |
| 1   |              | 8       |        |
|     |              |         | 8      |

The loop stops when `n` reaches 1, after 8 steps. (Different people lay out trace tables slightly differently, e.g. some put each pass of the loop on a single row. That's fine, as long as it's clear what value each variable has at each point.)

This program is based on the _Collatz conjecture_: start with any positive whole number, and repeatedly halve it if it's even, or multiply it by 3 and add 1 if it's odd. Nobody has ever found a starting number that doesn't eventually reach 1, but nobody has managed to prove that it always happens either!
