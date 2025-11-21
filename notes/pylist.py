# Python List - Complete Notes with Examples

# RULE OF THUMB
# - Expressions do NOT modify the original list (they return new list)
# - If a method returns None → original list is modified
# - If a method returns something meaningful → original list is unchanged

########################################################
# 1️⃣ LIST CREATION
########################################################

# Create an empty list
l1 = []

# Create an empty list using list() constructor
l2 = list()

# Create a list using list() with an iterable
l3 = list((1, 2, 3))  # tuple converted to list

# Create a list of squares from 1 to 9 using list comprehension
l4 = [x * x for x in range(1, 10)]  # [1,4,9,...,81]

########################################################
# 2️⃣ LIST OPERATIONS
########################################################

# Create a list of even numbers 2 to 20
evens = [x * 2 for x in range(1, 11)]  # [2,4,...,20]

# insert(index, element) → inserts value at specified index
# (MODIFIES THE LIST)
evens.insert(2, 8)  # Insert 8 at index 2

# remove(value) → removes first occurrence of value
# (MODIFIES THE LIST)
evens.remove(8)  # Removes the first 8

# del keyword → removes element by index
# (MODIFIES THE LIST)
del evens[4]  # Remove element at index 4

# del keyword with slicing → removes a range of items
# (MODIFIES THE LIST)
del evens[1:3]

# SLICING creates a NEW LIST
first5 = evens[:5]

# pop() removes last value and RETURNS it
removed_last = evens.pop()

# pop(index) removes value at index and RETURNS it
removed_index2 = evens.pop(2)

# Reverse with slicing → does NOT modify original list
rev_evens = evens[::-1]

########################################################
# 3️⃣ ACCESSING ELEMENTS
########################################################

nums = list(range(1, 13))  # [1..12]

# Access element at index 4
item_4 = nums[4]

# Access last element
last = nums[-1]

# Access second last element
second_last = nums[-2]

# Modify index 2 value
nums[2] = 1000

# Check membership using 'in'
if 4 in nums:
    found_msg = "Found"
else:
    found_msg = "Not Found"

########################################################
# 4️⃣ LIST SLICING
########################################################

lst = [1, 2, 4, 4, 5, 4, 7, 8, 9, 10, 11, 12]

# Slice: index 2 to 6
slice_1 = lst[2:7]

# Slice backwards: index 7 to 2 backwards
slice_2 = lst[7:1:-1]

########################################################
# 5️⃣ ADD / EXTEND / CONCATENATE
########################################################

lst2 = [1, 2, 3]

# append() → adds single element at end (MODIFIES LIST)
lst2.append(1009)

# extend() → adds multiple elements (MODIFIES LIST)
lst2.extend([100, 101])

# + operator creates NEW list aka concatenation of lists
lst3 = lst2 + [102, 103]

########################################################
# 6️⃣ COUNT AND COPY
########################################################

lst4 = [1, 2, 4, 4, 5, 4]

# count(value) → returns occurrences
count_4 = lst4.count(4)

# copy() → creates NEW SHALLOW COPY
copy1 = lst4.copy()
copy2 = lst4[:]

########################################################
# 7️⃣ ORDERING OPERATIONS
########################################################

# reverse() → MODIFIES LIST
lst4.reverse()

# repetition using * → creates NEW LIST
repeated = [3] * 10  # [3,3,...]

# sort() → MODIFIES LIST
sortable = [2, 9, 4, 1]
sortable.sort()  # ascending sort

########################################################
# END OF NOTES
########################################################
