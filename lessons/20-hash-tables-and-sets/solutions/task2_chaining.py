def hash_string(key, size):
    """Returns an index between 0 and size - 1 for the string `key`"""
    total = 0
    for char in key:
        total = total + ord(char)
    return total % size


class HashTable:
    """A hash table that uses separate chaining"""

    def __init__(self, size):
        self.size = size
        self.slots = []
        for i in range(size):
            self.slots.append([])  # each slot holds a list of [key, value] pairs
        self.count = 0

    def put(self, key, value):
        """Adds the key-value pair, or updates the value if the key exists"""
        slot = self.slots[hash_string(key, self.size)]
        for pair in slot:
            if pair[0] == key:
                pair[1] = value
                return
        slot.append([key, value])
        self.count = self.count + 1

    def get(self, key):
        """Returns the value for `key`"""
        slot = self.slots[hash_string(key, self.size)]
        for pair in slot:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def remove(self, key):
        """Removes `key` and its value"""
        slot = self.slots[hash_string(key, self.size)]
        for i in range(len(slot)):
            if slot[i][0] == key:
                slot.pop(i)
                self.count = self.count - 1
                return
        raise KeyError(key)

    def __contains__(self, key):
        slot = self.slots[hash_string(key, self.size)]
        for pair in slot:
            if pair[0] == key:
                return True
        return False

    def __len__(self):
        return self.count


extensions = HashTable(7)
for name, extension in [("Ada", 120), ("Alan", 101), ("Grace", 133), ("Tim", 155), ("Guido", 204), ("Margaret", 217)]:
    extensions.put(name, extension)

print(extensions.slots[0])       # [['Guido', 204], ['Margaret', 217]]
print(extensions.get("Grace"))   # 133
print(extensions.get("Margaret"))  # 217 (found in the chain at index 0)

extensions.put("Ada", 999)       # update an existing key
print(extensions.get("Ada"))     # 999
print(len(extensions))           # 6 (updating doesn't add a new pair)

extensions.remove("Guido")
print("Guido" in extensions, "Margaret" in extensions)  # False True
print(len(extensions))           # 5

try:
    extensions.get("Linus")
except KeyError as error:
    print(f"KeyError: {error}")
