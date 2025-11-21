# Python Tuple - Complete Notes with Examples

# RULE OF TUPLES
# - Tuples are immutable → Elements cannot be changed once created
# - Reassignment of the entire tuple is allowed
# - Tuples allow duplicate values
# - Operations that modify tuple do NOT exist (very few methods)

########################################################
# 1️⃣ TUPLE CREATION
########################################################

# Create an empty tuple
t1 = ()
t2 = tuple()

# Create tuple with values
t3 = (1, 2, 3)

# Create tuple using tuple() with an iterable (list converted to tuple)
t4 = tuple([4, 5, 6])

# Reassign whole tuple → Allowed
# NOTE: This creates a NEW tuple and updates reference
t4 = (7, 8, 9)

########################################################
# 2️⃣ TUPLE FROM COMPREHENSION
########################################################
# Create a tuple of even numbers (0-20)
# tuple() must be used because generator alone is NOT a tuple
t1 = tuple(x for x in range(21) if x % 2 == 0)

########################################################
# 3️⃣ ACCESSING TUPLE ELEMENTS
########################################################

# Access element by index
test = (11, 22, 33, 44)
elem_2 = test[2]   # 33

# Access last element
last_elem = test[-1]  # 44

# Tuples are immutable → index assignment NOT allowed
# test[2] = 100  # ❌ TypeError

########################################################
# 4️⃣ TUPLES CAN HAVE DUPLICATES
########################################################

t5 = (1, 2, 5, 4, 5)  # duplicates allowed

########################################################
# 5️⃣ TUPLE METHODS (ONLY TWO!)
########################################################

# index(value) → returns first index of element
idx_5 = t5.index(5)  # 2

# index(value) error when not found
# t5.index(10)  # ❌ ValueError

# count(value) → returns number of occurrences
count_5 = t5.count(5)  # 2

########################################################
# END OF NOTES
########################################################
