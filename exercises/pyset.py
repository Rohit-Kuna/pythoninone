# Python Set Practice Exercises - Follow Instructions
# Practice all key Set operations and master set behavior 🧠🔥
# Remember: Sets are unordered and contain only UNIQUE elements

# RULES OF SETS
# - Stores unordered unique elements
# - Does NOT allow duplicates
# - Elements must be hashable (immutable)
# - Supports mathematical set operations (union, intersection, difference)

########################################################
# 1️⃣ SET CREATION
########################################################

# create an empty set using set() → {} creates a dict, not set
s0=set()

# create a set with numbers 1,2,3 using {}
s2 = {1,2,3}

# create a set with numbers 4,5,6 using set() and passing an iterator
s2 = set([4,5,6])

# create a set from list [2,2,3,4] and ensure duplicates are removed
s3 = set([2,2,3,4])

# create a set of odd numbers between 1-15 using comprehension
# 👉 Use: {expr for var in iterable if condition}
s4 = {x for x in range(1,16) if x%2!=0}

########################################################
# 2️⃣ ADDING & REMOVING ELEMENTS
########################################################

s5 = {10, 20, 30}

# add 40 into s5 using add()
s5.add(4)

# add [50,60] using update(), used to add multiple iterables at once into a set
s5.update([50,60])

# add [70,30] , (78,45) in s5 using update()
s5.update([70,30],(78,45))
# print(s5) # OP: {4, 70, 10, 45, 78, 50, 20, 60, 30}

# remove 20 using remove()  # risky → error if not present
s5.remove(20) # ValueError if not present

# remove 999 using discard() → no error
s5.discard(999) 

# pop() → pop & return RANDOM element → store in removed_val
removed_val = s5.pop() # Random because set is unordered

########################################################
# 3️⃣ MEMBERSHIP TESTING
########################################################

# check if 30 exists in s5 → print Found
if 30 in s5:
    print("Found")

########################################################
# 4️⃣ SET OPERATIONS (union, intersection, etc.)
########################################################

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union() → returns all unique elements from both sets
U = A.union(B)

# intersection() → returns only common elements
I = A.intersection(B)

# difference() → elements present in A but not in B
D = A.difference(B)

# symmetric_difference() → elements that are NOT common in both sets
SD = A.symmetric_difference(B)

########################################################
# 5️⃣ IN-PLACE SET OPERATIONS (MODIFY ORIGINAL)
########################################################

C = {1, 2, 3, 4}
D2 = {3, 4, 5}

# update() → adds elements from another set (in-place union)
C.update(C.union(D2))
C.clear() # reset c

C = {1, 2, 3, 4}
# intersection_update() → keep only common elements (modifies original)
C.intersection_update(D2)
C.clear() # reset c

C = {1, 2, 3, 4}
# difference_update() → remove common elements (modifies original)
C.difference_update(D2)
C.clear() # reset c

C = {1, 2, 3, 4}
# symmetric_difference_update() → keep only non-common elements (modifies original)
C.symmetric_difference_update(D2)

########################################################
# 6️⃣ SUBSET / SUPERSET / DISJOINT
########################################################

X = {1, 2}
Y = {1, 2, 3, 4}
Z = {7, 8}

# issubset() → True if all elements of X exist in Y
is_sub = X.issubset(Y)

# issuperset() → True if Y contains all elements of X
is_super = Y.issuperset(X)

# isdisjoint() → True if no common elements
is_disjoint = X.isdisjoint(Z)

########################################################
# 7️⃣ COPY & CLEAR
########################################################

# create a copy of A → store in A_copy
A_copy = A.copy()

# clear all elements of A_copy
A_copy.clear()

########################################################
# 8️⃣ LENGTH, MIN, MAX
########################################################

Snums = {5, 2, 9, 1}

# find length
size = len(Snums)

# find minimum
mn = min(Snums)

# find maximum
mx = max(Snums)

########################################################
# 9️⃣ CONVERT BETWEEN SET & OTHER TYPES
########################################################

# convert list [1,2,2,3] to set
s_conv = set([1,2,2,3])

# convert set Snums to list
list_conv = list(Snums)

########################################################
# 🔟 BONUS CHALLENGE 💥
########################################################

# Remove all even numbers from s4 (use a loop OR comprehension)
ans = {x for x in s4 if x % 2 != 0}

# END OF EXERCISES 🎯 Good Luck!
