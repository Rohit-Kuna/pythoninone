# min heap
import heapq
minheap=[]

# push in heap
arr=[20,40,60,10,30]
for x in arr:
    heapq.heappush(minheap,x)

# heap top / peek
minheap[0]

# pop from heap
heapq.heappop(minheap) # 10

# heapify a list of items
nums = [8, 3, 7, 9, 4]
heapq.heapify(nums)

print(nums)  # This is the heap

# max heap

maxheap=[]
for x in arr:
    heapq.heappush(maxheap,-x)

# heap top / peek
print(-maxheap[0])

# pop from heap
heapq.heappop(maxheap) # 60


