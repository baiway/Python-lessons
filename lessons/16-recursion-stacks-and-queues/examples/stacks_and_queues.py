from collections import deque

# A list makes a perfectly good stack
stack = []
stack.append("a")  # push
stack.append("b")
stack.append("c")
print(stack.pop())  # pops "c": the last item pushed
print(stack[-1])    # peeks at "b", without removing it

# A deque makes a good queue
queue = deque()
queue.append("Ada")      # enqueue
queue.append("Alan")
queue.append("Grace")
print(queue.popleft())   # dequeues "Ada": the first item added
print(queue[0])          # peeks at "Alan", without removing him
