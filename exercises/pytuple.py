# Python Tuple Practice Exercises - Follow Instructions
# Practice every important tuple concept and operation 🧠💪
# Remember: Tuples are IMMUTABLE → cannot change elements once created!

########################################################
# 1️⃣ TUPLE CREATION
########################################################

# create an empty tuple using ()
t1 = ()

# create an empty tuple using tuple()
t1 = tuple()

# create a tuple with numbers 1,2,3
t2 = (1,2,3)

# create a tuple using tuple() function converting a list [4,5,6]
t3 = tuple([456])

# create a tuple of squares 1 to 5 using comprehension
# 👉 Use tuple() around generator expression
t4 = tuple(x*x for x in range(1,5))

########################################################
# 2️⃣ ACCESSING ELEMENTS
########################################################

test = (10, 20, 30, 40, 50)

# access element at index 2
idx_value = test[2]

# access last element
last_val = test[-1]

# access second last element
sec_last = test[-2]

########################################################
# 3️⃣ IMMUTABILITY CHECK
########################################################

# try changing index 2 → comment what happens
# test[2] = 999  # ❌ Write comment here: Duplicates not allowed

########################################################
# 4️⃣ COUNT & INDEX METHODS
########################################################

nums = (1, 3, 3, 4, 3, 5)

# count occurrences of 3, applying count()
count3 = nums.count(3)

# find index of first occurrence of 4, applying index()
idx4 = nums.index(4)

# try using index() for a value not present → comment the error
# nums.index(10)  # ❌ Write error comment : index out of bounds

########################################################
# 5️⃣ DUPLICATES & LENGTH
########################################################

t_dup = (5, 5, 5, 7, 8)

# get length of tuple using len()
t_len = len(t_dup)

########################################################
# 6️⃣ TUPLE PACKING & UNPACKING
########################################################

# tuple packing
t_packed = 10, 20, 30
a,b,c = t_packed

# unpack into three variables → a,b,c


########################################################
# 7️⃣ CONCATENATION & REPETITION
########################################################

a = (1, 2)
b = (3, 4)

# concatenate tuples into c
c = a+b

# repeat tuple a three times into r
r = c*3
print(r)

########################################################
# 8️⃣ MEMBERSHIP TEST
########################################################

# check if 50 exists in t_packed
# print Found if yes
if 50 in t_packed:
    print("Found")

########################################################
# 9️⃣ NESTED TUPLES
########################################################

nested = (1, 2, (10, 20, 30))

# access value 20 from nested tuple
nested_val = nested[2][1]

########################################################
# 🔟 TYPE CONVERSION
########################################################

# convert list [9,8,7] to tuple and store in t_conv
t_conv = tuple([9,8,7])

########################################################
# 1️⃣1️⃣ TUPLE VS LIST TEST
########################################################

# create a list and a tuple with same values
x_list = [1, 2, 3]
x_tuple = (1, 2, 3)

# try modifying list index 1
# try modifying tuple index 1 → note the difference in comments

########################################################
# END OF EXERCISES 🎯
########################################################