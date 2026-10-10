class HashSet:
    """A set, implemented as a hash table with separate chaining"""

    def __init__(self, size=11):
        self.size = size
        self.slots = [[] for i in range(size)]

    def _slot(self, item):
        # Python's `hash` works for any immutable item, not just strings
        return self.slots[hash(item) % self.size]

    def add(self, item):
        slot = self._slot(item)
        if item not in slot:  # each item is only stored once
            slot.append(item)

    def remove(self, item):
        slot = self._slot(item)
        if item not in slot:
            raise KeyError(item)
        slot.remove(item)

    def __contains__(self, item):
        return item in self._slot(item)

    def to_list(self):
        items = []
        for slot in self.slots:
            items.extend(slot)
        return items

    def union(self, other):
        result = HashSet()
        for item in self.to_list() + other.to_list():
            result.add(item)
        return result

    def intersection(self, other):
        result = HashSet()
        for item in self.to_list():
            if item in other:
                result.add(item)
        return result

    def difference(self, other):
        result = HashSet()
        for item in self.to_list():
            if item not in other:
                result.add(item)
        return result

    def is_subset(self, other):
        for item in self.to_list():
            if item not in other:
                return False
        return True


def make_set(items):
    result = HashSet()
    for item in items:
        result.add(item)
    return result


a = make_set([1, 2, 3, 3, 3])
b = make_set([2, 3, 4])

print(sorted(a.to_list()))                  # [1, 2, 3] (no duplicates)
print(sorted(a.union(b).to_list()))         # [1, 2, 3, 4]
print(sorted(a.intersection(b).to_list()))  # [2, 3]
print(sorted(a.difference(b).to_list()))    # [1]
print(make_set([2, 3]).is_subset(a))        # True
print(b.is_subset(a))                       # False

a.remove(1)
print(1 in a, 2 in a)                       # False True
