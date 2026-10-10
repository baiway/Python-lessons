class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def make_circle(items):
    """Creates a circular linked list, and returns its first node"""
    head = Node(items[0])
    current = head
    for item in items[1:]:
        current.next = Node(item)
        current = current.next
    current.next = head  # the last node points back to the first
    return head


def pass_the_parcel(players, k):
    """Returns the winner of pass the parcel, if the music stops every `k` passes"""
    holder = make_circle(players)

    # We need the node BEFORE the holder, so that we can remove the holder.
    # At the start, that's the last player in the circle.
    previous = holder
    while previous.next is not holder:
        previous = previous.next

    # Keep going until only one player is left (i.e. they point to themselves)
    while holder.next is not holder:
        for i in range(k):
            previous = holder
            holder = holder.next
        print(f"{holder.data} is out!")
        previous.next = holder.next  # remove the holder from the circle
        holder = holder.next         # pass the parcel to the next player

    return holder.data


winner = pass_the_parcel(["Ada", "Alan", "Grace", "Tim", "Linus"], 3)
print(f"{winner} wins!")
