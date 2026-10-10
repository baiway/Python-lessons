def hash_string(key, size):
    """Returns an index between 0 and size - 1 for the string `key`"""
    total = 0
    for char in key:
        total = total + ord(char)
    return total % size


class HashTable:
    """A hash table that uses separate chaining, and resizes itself"""

    MAX_LOAD_FACTOR = 0.75

    def __init__(self, size=4):
        self.size = size
        self.slots = [[] for i in range(size)]
        self.count = 0

    def load_factor(self):
        return self.count / self.size

    def put(self, key, value):
        """Adds the key-value pair, or updates the value if the key exists"""
        slot = self.slots[hash_string(key, self.size)]
        for pair in slot:
            if pair[0] == key:
                pair[1] = value
                return

        # It's a new key: make room first if the table would get too full
        if (self.count + 1) / self.size > HashTable.MAX_LOAD_FACTOR:
            self._resize(self.size * 2)
            slot = self.slots[hash_string(key, self.size)]

        slot.append([key, value])
        self.count = self.count + 1

    def get(self, key):
        """Returns the value for `key`"""
        for pair in self.slots[hash_string(key, self.size)]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def _resize(self, new_size):
        """Moves every item into a new table with `new_size` slots"""
        old_slots = self.slots
        self.size = new_size
        self.slots = [[] for i in range(new_size)]
        for slot in old_slots:
            for key, value in slot:
                # Each key needs rehashing, because its index depends on the size
                self.slots[hash_string(key, new_size)].append([key, value])


table = HashTable()
for i in range(20):
    table.put(f"key{i}", i)
    print(f"{i + 1:2} items: size {table.size:2}, load factor {table.load_factor():.2f}")

# Check that every item can still be found after all that resizing
print(all([table.get(f"key{i}") == i for i in range(20)]))  # True
