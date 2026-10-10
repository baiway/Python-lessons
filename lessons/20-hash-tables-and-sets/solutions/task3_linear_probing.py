def hash_string(key, size):
    """Returns an index between 0 and size - 1 for the string `key`"""
    total = 0
    for char in key:
        total = total + ord(char)
    return total % size


class ProbingHashTable:
    """A hash table that uses open addressing with linear probing"""

    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def put(self, key, value):
        """Adds the key-value pair, or updates the value if the key exists"""
        index = hash_string(key, self.size)
        for i in range(self.size):  # probe at most `size` slots
            if self.keys[index] is None or self.keys[index] == key:
                self.keys[index] = key
                self.values[index] = value
                return
            index = (index + 1) % self.size
        raise OverflowError("The hash table is full")

    def get(self, key):
        """Returns the value for `key`"""
        index = hash_string(key, self.size)
        for i in range(self.size):
            if self.keys[index] is None:
                break  # an empty slot means the key isn't in the table
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        raise KeyError(key)


extensions = ProbingHashTable(7)
for name, extension in [("Ada", 120), ("Alan", 101), ("Grace", 133), ("Tim", 155), ("Guido", 204), ("Margaret", 217)]:
    extensions.put(name, extension)

print(extensions.keys)            # Margaret is in slot 1
print(extensions.get("Margaret"))  # 217

extensions.put("Linus", 188)      # fills the last free slot (5)
try:
    extensions.put("Bjarne", 300)
except OverflowError as error:
    print(f"Error: {error}")
