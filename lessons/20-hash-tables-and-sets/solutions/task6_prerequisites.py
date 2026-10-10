def can_take(completed, prerequisites):
    """Returns `True` if every prerequisite has been completed"""
    return prerequisites <= completed  # i.e. prerequisites is a subset of completed


def missing(completed, prerequisites):
    """Returns the set of prerequisites that haven't been completed"""
    return prerequisites - completed


prerequisites = {"Programming 1", "Maths 1", "Data Structures"}
ada = {"Programming 1", "Maths 1", "Data Structures", "Databases"}
alan = {"Programming 1", "Networks"}

print(can_take(ada, prerequisites))         # True
print(sorted(missing(ada, prerequisites)))  # []
print(can_take(alan, prerequisites))        # False
print(sorted(missing(alan, prerequisites)))  # ['Data Structures', 'Maths 1']
