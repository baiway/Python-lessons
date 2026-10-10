import pytest

from sorting import bubble_sort


@pytest.mark.parametrize("items", [
    [],                     # empty list
    [1],                    # one item
    [1, 2, 3, 4, 5],        # already sorted
    [5, 4, 3, 2, 1],        # reverse order
    [2, 1],                 # the smallest list that needs a swap
    [3, 1, 2],
    [4, 2, 4, 1, 2],        # duplicates
    [-3, 10, 0, -7, 5],     # negative numbers
    ["pear", "apple", "fig"],
])
def test_bubble_sort(items):
    expected = sorted(items)  # we trust Python's built-in `sorted`
    bubble_sort(items)
    assert items == expected


# The buggy version passes the tests for [], [1] and [1, 2, 3, 4, 5], but
# fails all the others. Its inner loop was `range(n - pass_number - 1)`, which
# stops one comparison too early, so it never compares the last two items it
# should. The fix is `range(n - pass_number)`.
