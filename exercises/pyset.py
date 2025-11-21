# Python Set Practice Exercises - Follow Instructions
# Practice all key Set operations and master set behavior 🧠🔥
# Remember: Sets are unordered and contain only UNIQUE elements

########################################################
# 1️⃣ SET CREATION
########################################################

# create an empty set (NOT {})
s1 = 

# create a set with numbers 1,2,3
s2 = 

# create a set from list [2,2,3,4] and ensure duplicates are removed
s3 = 

# create a set of odd numbers between 1-15 using comprehension
# 👉 Use: {expr for var in iterable if condition}
s4 = 

########################################################
# 2️⃣ ADDING & REMOVING ELEMENTS
########################################################

s5 = {10, 20, 30}

# add 40 into s5

# add 50 and 60 using update()

# remove 20 using remove()  # risky → error if not present

# remove 999 using discard() → no error

# pop() → remove & return RANDOM element → store in removed_val
removed_val = 

########################################################
# 3️⃣ MEMBERSHIP TESTING
########################################################

# check if 30 exists in s5 → print Found/Not Found

########################################################
# 4️⃣ SET OPERATIONS (union, intersection, etc.)
########################################################

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# find union of A & B → store in U
U = 

# find intersection of A & B → store in I
I = 

# find elements in A not in B → store in D
D = 

# find symmetric difference → store in SD
SD = 

########################################################
# 5️⃣ IN-PLACE SET OPERATIONS (MODIFY ORIGINAL)
########################################################

C = {1, 2, 3, 4}
D2 = {3, 4, 5}

# update C with union of C and D2

# reset C = {1,2,3,4}
C = {1, 2, 3, 4}
# keep only common elements with D2 using intersection_update

# reset C again
C = {1, 2, 3, 4}
# remove common elements with D2 using difference_update

# reset C
C = {1, 2, 3, 4}
# apply symmetric_difference_update

########################################################
# 6️⃣ SUBSET / SUPERSET / DISJOINT
########################################################

X = {1, 2}
Y = {1, 2, 3, 4}
Z = {7, 8}

# check if X is subset of Y → store in is_sub
is_sub = 

# check if Y is superset of X → store in is_super
is_super = 

# check if X is disjoint with Z → store in is_disjoint
is_disjoint = 

########################################################
# 7️⃣ COPY & CLEAR
########################################################

# create a copy of A → store in A_copy
A_copy = 

# clear all elements of A_copy

########################################################
# 8️⃣ LENGTH, MIN, MAX
########################################################

Snums = {5, 2, 9, 1}

# find length
size = 

# find minimum
mn = 

# find maximum
mx = 

########################################################
# 9️⃣ CONVERT BETWEEN SET & OTHER TYPES
########################################################

# convert list [1,2,2,3] to set
s_conv = 

# convert set Snums to list
list_conv = 

########################################################
# 🔟 BONUS CHALLENGE 💥
########################################################

# Remove all even numbers from s4 (use a loop OR comprehension)


# END OF EXERCISES 🎯 Good Luck!