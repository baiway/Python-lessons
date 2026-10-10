# Task 1 solution
| Word  | Sum of character codes | Index (sum % 7) |
|-------|------------------------|-----------------|
| `cat` | 99 + 97 + 116 = 312    | 4               |
| `act` | 97 + 99 + 116 = 312    | 4               |
| `dog` | 100 + 111 + 103 = 314  | 6               |
| `god` | 103 + 111 + 100 = 314  | 6               |
| `bee` | 98 + 101 + 101 = 300   | 6               |
| `emu` | 101 + 109 + 117 = 327  | 5               |
| `owl` | 111 + 119 + 108 = 338  | 2               |

**(a) Separate chaining:** each word goes into the list at its index.

| Index | Contents                   |
|-------|----------------------------|
| 0     | `[]`                       |
| 1     | `[]`                       |
| 2     | `["owl"]`                  |
| 3     | `[]`                       |
| 4     | `["cat", "act"]`           |
| 5     | `["emu"]`                  |
| 6     | `["dog", "god", "bee"]`    |

**(b) Linear probing:** each word goes into the first free slot, starting at its index.
- `cat` → 4.
- `act` → 4 is taken, so 5.
- `dog` → 6.
- `god` → 6 is taken, so wrap around to 0.
- `bee` → 6 and 0 are taken, so 1.
- `emu` → 5 (taken by `act`), 6, 0 and 1 are all taken, so 2.
- `owl` → 2 is taken (by `emu`), so 3.

| Index | 0     | 1     | 2     | 3     | 4     | 5     | 6     |
|-------|-------|-------|-------|-------|-------|-------|-------|
| Word  | `god` | `bee` | `emu` | `owl` | `cat` | `act` | `dog` |

Notice how `emu` and `owl` end up a long way from their "home" slots, because earlier collisions filled up the slots they should have gone in. This is the clustering problem with linear probing.

`cat` and `act` always collide because they contain the same letters, and adding up the character codes gives the same total whatever order the letters are in. So any two anagrams have the same hash, whatever the size of the table! A better hash function takes the _position_ of each character into account, e.g. by multiplying the running total by a number (such as 31) before adding each character's code.
