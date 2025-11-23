########################################################
# PYTHON TUPLES — EXERCISE SHEET
########################################################
# RULES OF TUPLES:
# - Tuples are IMMUTABLE → cannot modify elements once created
# - Faster and more memory-efficient than lists
# - Used for fixed data
########################################################



########################################################
# SECTION 1: TUPLE CREATION & BASIC ACCESS
########################################################

# TODO: Create an empty tuple using tuple()
# t0 = tuple()
# print(t0)

# TODO: Create a tuple t1 with values (1, 2, 3)
# t1 = (1, 2, 3)
# print(t1)

# TODO: Create tuple t2 from list [4, 5, 6] using tuple()
# t2 = tuple([4, 5, 6])
# print(t2)

# TODO: Create tuple t3 of squares from 1 to 5 using tuple() + generator expression
# t3 = tuple(x * x for x in range(1, 6))
# print(t3)

test = (10, 20, 30, 40, 50)

# TODO: Access element at index 2 and print
# val = test[2]
# print(val)

# TODO: Access last element using negative index and print
# last = test[-1]
# print(last)



########################################################
# SECTION 2: IMMUTABILITY TEST
########################################################

immutable_tup = (10, 20, 30)

# TODO: Try modifying index 1 and write expected error in comment
# immutable_tup[1] = 999  # ❌ TypeError: 'tuple' object does not support item assignment



########################################################
# SECTION 3: COUNT & INDEX OPERATIONS
########################################################

nums = (1, 3, 3, 4, 3, 5)

# TODO: Count occurrences of 3 in nums using count()
# count3 = nums.count(3)
# print(count3)

# TODO: Find index of first occurrence of 4 using index()
# idx4 = nums.index(4)
# print(idx4)

# TODO: Try using index() for value NOT in tuple → comment expected error
# nums.index(10)  # ❌ ValueError: tuple.index(x): x not in tuple



########################################################
# SECTION 4: MEMBERSHIP TEST
########################################################

colors = ("red", "green", "blue")

# TODO: Check if "green" exists in colors using 'in' and print message
# if "green" in colors:
#     print("Found")



########################################################
# SECTION 5: LENGTH OF TUPLE
########################################################

t_dup = (5, 5, 5, 7, 8)

# TODO: Print length of t_dup using len()
# length = len(t_dup)
# print(length)



########################################################
# SECTION 6: PACKING & UNPACKING USING * OPERATOR
########################################################

# TODO: Pack values into tuple t_pack WITHOUT parentheses
# t_pack = 10, 20, 30
# print(t_pack)

# TODO: Unpack t_pack into a, b, c
# a, b, c = t_pack
# print(a, b, c)

colors2 = ("black", "white", "green", "orange", "yellow")

# TODO: Unpack first two into f1,f2 and remaining into others using *
# f1, f2, *others = colors2
# print(f1, f2, others)

# TODO: Unpack first, middle group, and last using *
# first, *mid, last = colors2
# print(first, mid, last)



########################################################
# SECTION 7: CONCATENATION & REPETITION
########################################################

tA = (1, 2)
tB = (3, 4)

# TODO: Concatenate tA and tB using + operator → result tC
# tC = tA + tB
# print(tC)

# TODO: Repeat tuple tA three times using * operator → result tR
# tR = tA * 3
# print(tR)



########################################################
# SECTION 8: TYPE CONVERSION
########################################################

# TODO: Convert list [9, 8, 7] into tuple using tuple()
# t_conv = tuple([9, 8, 7])
# print(t_conv)



########################################################
# SECTION 9: NESTED TUPLES
########################################################

nested = (1, 2, (10, 20, 30))

# TODO: Access value 20 from nested tuple
# nested_val = nested[2][1]
# print(nested_val)



########################################################
# SECTION 10: TUPLE TO LIST AND BACK
########################################################

# TODO: Convert nested tuple into list → l_editable
# l_editable = list(nested)
# print(l_editable)

# TODO: Convert l_editable back to tuple → nested2
# nested2 = tuple(l_editable)
# print(nested2)



########################################################
# SECTION 11: FUNCTION RETURNING TUPLE (PACKING)
########################################################

# TODO: Write function get_info() returning tuple of 3 values
# def get_info():
#     return "Python", 3.11, "Programming"
#
# info = get_info()
# print(info)



########################################################
# SECTION 12: UNPACKING IN FUNCTIONS USING *
########################################################

# TODO: Define function show(a,b,c) and call it using unpack *
# def show(x, y, z):
#     print(x, y, z)
#
# show(*tA)  # tA = (1,2)



########################################################
# SECTION 13: TUPLE VS LIST MUTABILITY
########################################################

x_list = [1, 2, 3]
x_tuple = (1, 2, 3)

# TODO: Modify x_list index 1 to 999 → allowed
# x_list[1] = 999
# print(x_list)

# TODO: Modify x_tuple index 1 → write expected error comment
# x_tuple[1] = 999  # ❌ TypeError: 'tuple' object does not support item assignment



########################################################
# SECTION 14: USER INPUT + PACKING + UNPACKING
########################################################

# TODO:
# Step1: Take 3 numbers from user
# Step2: Pack into tuple tup
# Step3: Unpack into a,b,c using *
# Step4: Print values individually

# x = int(input("Enter number 1: "))
# y = int(input("Enter number 2: "))
# z = int(input("Enter number 3: "))
# tup = (x, y, z)
# a, b, c = tup
# print(a, b, c)



########################################################
# END OF TUPLE EXERCISES — GREAT WORK!
########################################################
