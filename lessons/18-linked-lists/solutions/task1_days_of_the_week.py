class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a node for each day, then link each one to the next
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
nodes = []
for day in days:
    nodes.append(Node(day))
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
head = nodes[0]

# Traverse the list, printing each day
current = head
while current is not None:
    print(current.data)
    current = current.next

# Traverse it again, counting the nodes
count = 0
current = head
while current is not None:
    count = count + 1
    current = current.next
print(f"There are {count} nodes in the list")
