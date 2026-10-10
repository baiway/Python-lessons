# Task 1 solution
Inserting 50, 30, 70, 20, 40, 60, 80, 35, 65:
```
            50
          /    \
        30      70
       /  \    /  \
     20   40  60   80
         /      \
       35        65
```

The tree has height 3 (e.g. 50 → 30 → 40 → 35), and the leaves are 20, 35, 65 and 80.

Inserting the same values in sorted order (20, 30, 35, 40, 50, 60, 65, 70, 80), each new value is bigger than everything already in the tree, so it always goes to the right of the last node:
```
20
  \
   30
     \
      35
        \
         40
           \
            50
              \
               60
                 \
                  65
                    \
                     70
                       \
                        80
```

This tree has height 8, and only one leaf (80). It's really just a linked list! Searching it takes up to 9 steps, compared with at most 4 for the first tree, even though both contain exactly the same values. The order in which values are inserted makes a big difference to the shape of a binary search tree (see "Balanced and unbalanced trees").
