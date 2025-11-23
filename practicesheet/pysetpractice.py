########################################################
# PYTHON SETS — EXERCISE SHEET
########################################################
# RULES OF SETS:
# - Unordered (no fixed positions / indexing)
# - UNIQUE elements only (duplicates are removed)
# - Mutable → can add/remove elements
# - Supports mathematical operations: union / intersection / diff
########################################################



########################################################
# SECTION 1: SET CREATION
########################################################

# TODO: Create an empty set using set()
# s0 = set()
# print(s0)

# TODO: Create a set s1 with values {1,2,3} using {}
# s1 = {1, 2, 3}
# print(s1)

# TODO: Create set s2 from list [2,2,3,4] and remove duplicates using set()
# s2 = set([2, 2, 3, 4])
# print(s2)

# TODO: Create a set of odd numbers 1–15 using set comprehension
# s3 = {x for x in range(1,16) if x % 2 != 0}
# print(s3)



########################################################
# SECTION 2: ADDING & REMOVING ELEMENTS
########################################################

s4 = {10, 20, 30}

# TODO: Add 40 to s4 using add()
# s4.add(40)
# print(s4)

# TODO: Add elements 50 & 60 using update() with list
# s4.update([50, 60])
# print(s4)

# TODO: Remove 20 using remove() → raise error if not present
# s4.remove(20)
# print(s4)  # comment: remove() raises ValueError if missing

# TODO: Remove 999 using discard() → no error if missing
# s4.discard(999)
# print(s4)

# TODO: Pop a random element using pop(), print removed + updated set
# removed = s4.pop()
# print(removed, s4)



########################################################
# SECTION 3: MEMBERSHIP TEST
########################################################

# TODO: Check if 30 exists in s4 using "in" and print message
# if 30 in s4:
#     print("Found")



########################################################
# SECTION 4: MATHEMATICAL SET OPERATIONS
########################################################

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# TODO: Get union using union()
# U = A.union(B)
# print(U)

# TODO: Get intersection using intersection()
# I = A.intersection(B)
# print(I)

# TODO: Get elements in A not in B using difference()
# D = A.difference(B)
# print(D)

# TODO: Get symmetric difference using symmetric_difference()
# SD = A.symmetric_difference(B)
# print(SD)



########################################################
# SECTION 5: IN-PLACE SET OPERATIONS (modify original set)
########################################################

C = {1, 2, 3, 4}
D2 = {3, 4, 5}

# TODO: Perform in-place union using update()
# C.update(D2)
# print(C)

# TODO: Keep only common elements using intersection_update()
# C.intersection_update(D2)
# print(C)

# Reset set
# C = {1, 2, 3, 4}

# TODO: Remove common elements using difference_update()
# C.difference_update(D2)
# print(C)

# Reset set
# C = {1, 2, 3, 4}

# TODO: Keep only non-common elements using symmetric_difference_update()
# C.symmetric_difference_update(D2)
# print(C)



########################################################
# SECTION 6: SUBSET / SUPERSET / DISJOINT
########################################################

X = {1, 2}
Y = {1, 2, 3, 4}
Z = {7, 8}

# TODO: Check if X is subset of Y using issubset()
# print(X.issubset(Y))

# TODO: Check if Y is superset of X using issuperset()
# print(Y.issuperset(X))

# TODO: Check if X and Z are disjoint using isdisjoint()
# print(X.isdisjoint(Z))



########################################################
# SECTION 7: COPY & CLEAR
########################################################

# TODO: Copy A into A_copy using copy()
# A_copy = A.copy()
# print(A_copy)

# TODO: Clear A_copy using clear()
# A_copy.clear()
# print(A_copy)



########################################################
# SECTION 8: LENGTH, MIN, MAX
########################################################

Nums = {5, 2, 9, 1}

# TODO: Print length using len()
# print(len(Nums))

# TODO: Print minimum using min()
# print(min(Nums))

# TODO: Print maximum using max()
# print(max(Nums))



########################################################
# SECTION 9: TYPE CONVERSIONS
########################################################

# TODO: Convert list [1,2,2,3] into set
# s_conv = set([1,2,2,3])
# print(s_conv)

# TODO: Convert set Nums into list using list()
# list_conv = list(Nums)
# print(list_conv)



########################################################
# SECTION 10: SET UNPACKING USING * OPERATOR
########################################################

# TODO: Unpack set A into a list using *
# lst_unpack = [*A]
# print(lst_unpack)

# TODO: Assign first element to f and rest to others using *
# f, *others = A  # order is arbitrary due to set nature
# print(f, others)



########################################################
# SECTION 11: BONUS — FILTERING with Comprehension
########################################################

# TODO: Remove all even numbers from range 1-20 using set comprehension
# s_even_removed = {x for x in range(1,21) if x % 2 != 0}
# print(s_even_removed)



########################################################
# END OF SET EXERCISES — EXCELLENT WORK!
########################################################
