# Lesson 20: Hash tables and sets
In [Lesson 13](../13-dictionaries-and-sets), we saw that looking something up in a dictionary or a set is very fast, much faster than searching a list, even for millions of items. In this lesson, we'll find out how this works, by building our own _hash table_: the data structure that Python uses behind the scenes for both dictionaries and sets. We'll then look at sets as an abstract data type.

## The idea
Suppose we want to store some people's phone extensions, so that we can look up anyone's extension by their name. If we stored the names in a list, we'd have to search through the list (in $O(n)$ time) to find the right one. But looking up an item in a list _by its index_ is instant. So what if we could turn each name into an index, and store each person at that index?

That's exactly what a hash table does. It stores its items in a list of a fixed size (the _table_, whose positions are often called _buckets_ or _slots_), and uses a _hash function_ to turn each key into the index where it should be stored.

## Hash functions
A hash function takes a key and turns it into a whole number. A very simple hash function for strings is to add up the character codes of all the characters (see [Lesson 7](../07-strings)), then use `%` to turn the total into an index between 0 and the size of the table minus 1:
```python
def hash_string(key, size):
    """Returns an index between 0 and size - 1 for the string `key`"""
    total = 0
    for char in key:
        total = total + ord(char)
    return total % size
```

With a table of size 7:

| Key        | Sum of character codes | Index (sum % 7) |
|------------|------------------------|-----------------|
| `Ada`      | 262                    | 3               |
| `Alan`     | 380                    | 2               |
| `Grace`    | 482                    | 6               |
| `Tim`      | 298                    | 4               |
| `Guido`    | 504                    | 0               |
| `Margaret` | 819                    | 0               |

To find Grace's extension, we don't need to search: we just calculate `hash_string("Grace", 7)`, which is 6, and look in slot 6.

A good hash function should:
1. Always give the same index for the same key (otherwise we'd never find anything again!).
2. Be quick to calculate.
3. Spread the keys out evenly across the table, so that as few keys as possible end up at the same index.

## Collisions
Unfortunately, Guido and Margaret both have an index of 0! When two keys hash to the same index, it's called a _collision_. Collisions can't be avoided completely: if there are more possible keys than slots in the table (and there almost always are), some of them must end up in the same slot. So a hash table needs a way of dealing with them. There are two common approaches.

### Separate chaining
In _separate chaining_, each slot in the table holds a list (or a linked list, as in [Lesson 18](../18-linked-lists)) of all the key-value pairs that hash to that index. To look up a key, we go to its slot and search through that slot's (hopefully short) list.

| Index | Contents                                  |
|-------|-------------------------------------------|
| 0     | `[("Guido", 204), ("Margaret", 217)]`     |
| 1     | `[]`                                      |
| 2     | `[("Alan", 101)]`                         |
| 3     | `[("Ada", 120)]`                          |
| 4     | `[("Tim", 155)]`                          |
| 5     | `[]`                                      |
| 6     | `[("Grace", 133)]`                        |

### Open addressing (linear probing)
In _open addressing_, each slot holds at most one item. If a key's slot is already taken, we look for another free slot using a fixed rule. The simplest rule is _linear probing_: try the next slot along, then the one after that, and so on (wrapping around to slot 0 at the end of the table), until we find a free one. This is sometimes called _rehashing_. Here, Margaret's slot (0) is taken by Guido, so Margaret goes in slot 1 instead:

| Index | 0                | 1                   | 2             | 3            | 4            | 5 | 6              |
|-------|------------------|---------------------|---------------|--------------|--------------|---|----------------|
| Key   | `Guido`          | `Margaret`          | `Alan`        | `Ada`        | `Tim`        |   | `Grace`        |

To look up a key, we start at its slot and probe in the same way until we either find the key, or reach an empty slot (in which case the key isn't in the table). Linear probing tends to create _clusters_ of full slots, which make probing slower, and deleting items is awkward: if you simply empty a slot, later searches might stop there too early. (The usual fix is to mark deleted slots with a special "deleted" marker, sometimes called a _tombstone_.)

You can find both versions of this example in [`examples/hash_tables.py`](examples/hash_tables.py).

**Task 1:** Using the `hash_string` function above with a table of size 7, work out the index for each of the words `cat`, `act`, `dog`, `god`, `bee`, `emu` and `owl`. Then, on paper, draw the hash table you get by inserting them in that order (a) using separate chaining and (b) using linear probing. Why do `cat` and `act` (and `dog` and `god`) always collide with this hash function, whatever the size of the table? [Solution](solutions/task1_hashing_by_hand.md)

**Task 2:** Write a `HashTable` class that uses separate chaining, with a table of a given `size`. Each slot should hold a Python list of `[key, value]` pairs. Give it the following methods: [Solution](solutions/task2_chaining.py)
- `put(key, value)`: adds the key-value pair, or updates the value if the key is already there.
- `get(key)`: returns the value for `key`, or raises a `KeyError` if it isn't there.
- `remove(key)`: removes `key` (and its value), or raises a `KeyError` if it isn't there.
- `__contains__(key)`: returns `True` if `key` is in the table. (Python calls this dunder method when you write `key in table`.)
- `__len__()`: returns the number of key-value pairs in the table.

**Task 3:** Write a `ProbingHashTable` class that uses linear probing instead. Give it `put(key, value)` and `get(key)` methods (you don't need to handle deleting), and make `put` raise an exception if the table is full. Test it with the names from the example above, and check that Margaret ends up in slot 1. [Solution](solutions/task3_linear_probing.py)

## Load factor and resizing
As a hash table fills up, collisions become more and more common: chains get longer, or probing has to check more and more slots. The _load factor_ measures how full a hash table is:

```math
\text{load factor} = \frac{\text{number of items}}{\text{number of slots}}
```

Hash tables are fast as long as the load factor stays low (a common rule of thumb is below about 0.7). When it gets too high, the table is _resized_: a new, bigger table is created (often twice the size), and every item is moved across to it. Each item has to be _rehashed_ (its index calculated again), because its index depends on the size of the table. Resizing is slow, but it happens rarely, so on average, adding, finding and removing items all take $O(1)$ time: they don't get slower as the table gets bigger. In the worst case (if every key collides), they can take $O(n)$ time, but with a good hash function, this is very unlikely.

**Task 4:** Add resizing to your `HashTable` class from Task 2: whenever adding a new key would make the load factor greater than 0.75, double the number of slots and rehash every item into the new table. Add a `load_factor()` method, and print the size and load factor of the table as you add 20 keys. [Solution](solutions/task4_resizing.py)

## Python's `hash` function, and why dictionary keys must be immutable
Python's dictionaries and sets are hash tables, with a much more sophisticated hash function than ours: you can call it yourself using `hash`. For example, `hash(42)` is `42`, and `hash("Ada")` is a large number. (For security reasons, string hashes are different every time you run Python, so you'll see a different number to me!)

This explains a rule from [Lesson 13](../13-dictionaries-and-sets): dictionary keys (and set items) must be immutable. Suppose you could use a list as a key. If you then changed the list, its hash would change, so the dictionary would look for it in the wrong slot, and you'd never find it again. To stop this from happening, Python simply refuses to hash mutable objects like lists, and gives you a `TypeError: unhashable type: 'list'`. Immutable objects like strings, numbers and tuples are fine.

## Sets
A _set_, as an abstract data type, is an unordered collection of unique items, which supports the following operations:
- **add** an item, **remove** an item, and check whether an item is in the set (often called **contains** or **membership**),
- **union**, **intersection** and **difference** of two sets (see [Lesson 13](../13-dictionaries-and-sets)),
- checking whether one set is a **subset** of another (every item in the first set is also in the second), or a **superset** (every item in the second set is also in the first).

A hash table is a natural way of implementing a set: it's just a hash table with keys and no values. Hashing makes checking whether an item is in the set an $O(1)$ operation, and also guarantees that each item is stored only once. In Python, you can check for subsets and supersets using `<=` and `>=` (or the methods `.issubset` and `.issuperset`):
```python
>>> {1, 2} <= {1, 2, 3}
True
>>> {1, 2, 3} >= {1, 4}
False
```

**Task 5:** Write a `HashSet` class using separate chaining (like your `HashTable`, but storing only items, without values). Give it `add`, `remove` and `__contains__` methods, and `union(other)`, `intersection(other)`, `difference(other)` and `is_subset(other)` methods, where `other` is another `HashSet`. The first three should return a new `HashSet`. Add a `to_list()` method so you can print the contents. Don't use Python's `set` anywhere! [Solution](solutions/task5_hash_set.py)

**Task 6:** To take a course, students must have completed all of its prerequisite modules. Using Python's sets, write a function `can_take(completed, prerequisites)` that returns `True` if a student can take a course, and a function `missing(completed, prerequisites)` that returns the set of modules they still need. Test them with the data below. [Solution](solutions/task6_prerequisites.py)
```python
prerequisites = {"Programming 1", "Maths 1", "Data Structures"}
ada = {"Programming 1", "Maths 1", "Data Structures", "Databases"}
alan = {"Programming 1", "Networks"}
```

**⭐ Task 7:** Use the `time` module (see [Lesson 10](../10-searching-and-sorting) Task 10) to compare how long it takes to check whether each of the numbers from 99,000 to 99,999 is in (a) a list and (b) a set, each containing the numbers from 0 to 99,999. How many times faster is the set? Why? [Solution](solutions/task7_list_vs_set.py)

**⭐ Task 8:** By default, two objects of your own classes are only equal (and only have the same hash) if they're the _same_ object. Write a `Point` class with `x` and `y` attributes, and add `__eq__` and `__hash__` methods so that points with the same coordinates are equal, and can be used as dictionary keys and stored in sets. Hint: `__hash__` can return `hash((self.x, self.y))`. Check that `{Point(1, 2), Point(1, 2), Point(3, 4)}` contains only two points. What would go wrong if you changed a point's `x` after putting it in a set? (A frozen dataclass from [Lesson 15](../15-type-hints-and-dataclasses) does all of this for you!) [Solution](solutions/task8_hashable_points.py)

---
[← Previous: Lesson 19](../19-binary-search-trees) | [Contents](../../README.md)
