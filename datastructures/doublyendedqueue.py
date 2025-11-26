from collections import deque
# Doubly ended queue

# create a queue
dq=deque()

# append to left
dq.appendleft(2)
dq.appendleft(3)

# apppend to right
dq.append(10)

# remove from left
dq.popleft()

# remove from right
dq.pop()

# size
size=len(dq)

# check if empty
if not dq:
    print("Empty")
    
# traverse normally as in list left to right / right to left

# dequeuing and traversing
dq=deque([10,40,82,56,8])
# traverse and dequeue
# keep removing/dequeing from left
while dq:
    item=dq.popleft()
    print(item)

dq=deque([10,40,82,56,8])
# keep removing/dequeing from right
while dq:
    item=dq.pop()
    print(item)