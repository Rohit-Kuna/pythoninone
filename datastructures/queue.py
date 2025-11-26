from collections import deque

# FIFO Queue
# left = front, right = back

# create a queue
q=deque()

# enque (add to right)
q.append(10)
q.append(20)
q.append(30)

# deque (remove from left)
q.popleft()

# peek leftmost
front=q[0]

# size
size=len(q)

# check if empty or not
if not q:
    print("Empty")
    
# traverse a queue
# traverse normally as queue is iterable
q1=deque([1,6,3,5,8])
for x in q1:
    print(x)
    
# keep dequeing from left
while q:
    item=q.popleft()
    print(item)
