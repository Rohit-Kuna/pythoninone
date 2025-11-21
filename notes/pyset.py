# Python Set - Complete Notes with Examples

# RULES OF SETS
# - Stores unordered unique elements
# - Does NOT allow duplicates
# - Elements must be hashable (immutable)
# - Supports mathematical set operations (union, intersection, difference)

########################################################
# 1️⃣ SET CREATION
########################################################

# Create an empty set using set() → {} creates a dict, not set
s1 = set()

# Create a set with elements
s2 = {1, 2, 3}

# Create a set from an iterable (list converted to set)
s3 = set([1, 2, 3, 4])

# Duplicate elements are removed automatically
s4 = {2, 4, 5, 2, 3, 5}  # → {2,3,4,5}

########################################################
# 2️⃣ SET COMPREHENSION
########################################################

# Create a set of even numbers
s5 = {x for x in range(1, 21) if x % 2 == 0}

########################################################
# 3️⃣ CHECK MEMBERSHIP (O(1))
########################################################

num_check = 3 in s5  # True or False

########################################################
# 4️⃣ MODIFYING SETS (In-place operations)
########################################################

s6 = {10, 20, 30}

# add(value) → inserts a single element
s6.add(40)

# update(iterable) → adds multiple elements
s6.update([50, 60])  # list or any iterable

# remove(value) → removes value, ERROR if not found
# s6.remove(100)  # ❌ KeyError if missing

# discard(value) → removes value, NO ERROR if not found
s6.discard(100)  # safe remove

# pop() → removes and returns a random element
removed_val = s6.pop()

# clear() → removes all elements
# s6.clear()

########################################################
# 5️⃣ SET OPERATIONS (RETURN NEW SETS)
########################################################

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union() → elements from both sets
union_set = A.union(B)  # {1,2,3,4,5,6}

# intersection() → common elements
intersection_set = A.intersection(B)  # {3,4}

# difference() → elements only in A not in B
difference_set = A.difference(B)  # {1,2}

# symmetric_difference() → unique elements in each
symmetric_diff = A.symmetric_difference(B)  # {1,2,5,6}

########################################################
# 6️⃣ IN-PLACE SET OPERATIONS
########################################################

C = {1, 2, 3, 4}
D = {3, 4, 5}

# update with union
C.update(D)  # C becomes {1,2,3,4,5}

# intersection_update → keep only common elements
C = {1, 2, 3, 4}
C.intersection_update(D)  # {3,4}

# difference_update → remove common elements
C = {1, 2, 3, 4}
C.difference_update(D)  # {1,2}

# symmetric_difference_update → keep only unique ones
C = {1, 2, 3, 4}
C.symmetric_difference_update(D)  # {1,2,5}

########################################################
# 7️⃣ SUBSET / SUPERSET / DISJOINT
########################################################

X = {1, 2}
Y = {1, 2, 3, 4}
Z = {5, 6}

# issubset() → checks if subset
is_sub = X.issubset(Y)  # True

# issuperset() → checks if superset
is_super = Y.issuperset(X)  # True

# isdisjoint() → True if no common elements
is_disjoint = X.isdisjoint(Z)  # True

########################################################
# END OF NOTES
########################################################
