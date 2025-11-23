########################################################
# RULES OF PYTHON LISTS
########################################################
# - Expressions return new lists → original list unchanged
# - Methods that modify list return None → original list changes
# - IMPORTANT: Always check return values before assuming behavior
########################################################



########################################################
# SECTION 1: LIST CREATION & BASIC ACCESS
########################################################

# TODO: Create an empty list named l0 using list()
# l0 = list()
# print(l0)

# TODO: Create a list num with values 1 to 5 using []
# num = [1, 2, 3, 4, 5]
# print(num)

# TODO: Create list num2 using list() and range() for 1 to 5
# num2 = list(range(1, 6))
# print(num2)

# TODO: Create a list l1 of even numbers 2 to 20 using list comprehension
# l1 = [x for x in range(2, 21, 2)]
# print(l1)

# TODO: Access element at index 3 of l1 and print it
# x = l1[3]
# print(x)

# TODO: Access last element of l1 using negative index
# last = l1[-1]
# print(last)

# TODO: Change value at index 2 of l1 to 20
# l1[2] = 20
# print(l1)



########################################################
# SECTION 2: ADD & REMOVE ITEMS
########################################################

# TODO: Add 100 at end of l1 using append()
# l1.append(100)
# print(l1)

# TODO: Add 200 and 300 at end using extend()
# l1.extend([200, 300])
# print(l1)

# TODO: Insert 999 at index 1 using insert()
# l1.insert(1, 999)
# print(l1)

# TODO: Remove first occurrence of 8 using remove()
# l1.remove(8)
# print(l1)

# TODO: Remove element at index 4 using del keyword
# del l1[4]
# print(l1)

# TODO: Remove last element using pop() and print removed + updated list
# removed_last = l1.pop()
# print(removed_last, l1)

# TODO: Remove element at index 2 using pop() and print removed + updated list
# removed_middle = l1.pop(2)
# print(removed_middle, l1)



########################################################
# SECTION 3: SLICING OPERATIONS
########################################################

# TODO: Create a slice of first 5 elements → slice1
# slice1 = l1[:5]
# print(slice1)

# TODO: Reverse first 6 elements using slicing → rev_slice
# rev_slice = l1[5::-1]
# print(rev_slice)

# TODO: Delete slice index 1 to 3 using del with slice
# del l1[1:4]
# print(l1)



########################################################
# SECTION 4: SEARCHING & COUNTING
########################################################

# TODO: Check if 10 exists in l1 and print message using "in"
# if 10 in l1:
#     print("10 Found")

# TODO: Count number of occurrences of 4 using count()
# count4 = l1.count(4)
# print(count4)

# TODO: Find index of 20 using index()
# index20 = l1.index(20)
# print(index20)



########################################################
# SECTION 5: COPYING LISTS
########################################################

# TODO: Create copy of l1 → l2 using copy()
# l2 = l1.copy()
# print(l2)

# TODO: Create copy of l1 → l3 using slicing
# l3 = l1[:]
# print(l3)



########################################################
# SECTION 6: ORDER METHODS
########################################################

nums = [5, 2, 9, 1, 7]

# TODO: Reverse nums using reverse()
# nums.reverse()
# print(nums)

# TODO: Sort nums in ascending order using sort()
# nums.sort()
# print(nums)

nums2 = [4, 2, 6, 3, 8]

# TODO: Create sorted copy of nums2 using sorted()
# sorted_nums = sorted(nums2)
# print(sorted_nums)



########################################################
# SECTION 7: CONCATENATION & REPETITION
########################################################

l4 = [1, 2, 3]
l5 = [4, 5]

# TODO: Concatenate lists l4 & l5 using + operator → l6
# l6 = l4 + l5
# print(l6)

# TODO: Create list named zeros with five 0s using *
# zeros = [0] * 5
# print(zeros)



########################################################
# SECTION 8: CLEAR / DELETE
########################################################

# TODO: Clear list l5 using clear()
# l5.clear()
# print(l5)

# TODO: Delete all items in l6 using del and slicing
# del l6[:]
# print(l6)



########################################################
# SECTION 9: BONUS — COMPREHENSION
########################################################

# TODO: Remove all 4s from l1 using list comprehension
# l1 = [x for x in l1 if x != 4]
# print(l1)



########################################################
# SECTION 10: PACKING & UNPACKING USING * OPERATOR
########################################################

colors = ["red", "green", "blue"]
# TODO: Unpack into c1, c2, c3 using unpacking
# c1, c2, c3 = colors
# print(c1, c2, c3)

numbers = [10, 20, 30, 40, 50]
# TODO: Unpack first two into n1,n2 and rest into others using *
# n1, n2, *others = numbers
# print(n1, n2, others)

a, b = 5, 10
# TODO: Swap a and b using unpacking
# a, b = b, a
# print(a, b)

names = ["Mr", "Rohit", "Kuna", "Fullstack", "Engineer"]
# TODO: Unpack first, middle values, last using *
# title, first, *mid, last = names
# print(title, first, mid, last)

scores = [98, 85, 90, 92, 88]
# TODO: Unpack first, middles, last using *
# s1, *s_mid, s_last = scores
# print(s1, s_mid, s_last)

data = [101, "Laptop", 55000, "Electronics", "India"]
# TODO: Extract id and price only using unpacking and _ for unused
# id, _, price, *_ = data
# print(id, price)

x, y, z, w = "Python", "Java", "C++", "JavaScript"
# TODO: Pack into list langs
# langs = [x, y, z, w]
# print(langs)

list1 = [1, 2]
list2 = [3, 4]
# TODO: Merge using * operator
# packed_list = [*list1, *list2]
# print(packed_list)



########################################################
# SECTION 11: UNPACKING IN FUNCTIONS USING *
########################################################

def display(a, b, c):
    print(a, b, c)

values = [100, 200, 300]

# TODO: Call display using unpacking operator *
# display(*values)

# TODO: Create print_nums() using *args & print all values
# def print_nums(*args):
#     print(args)
# print_nums(10, 20, 30)



########################################################
# SECTION 12: USER INPUT + PACKING + UNPACKING
########################################################

# TODO:
# Step1: Create empty list nums
# Step2: Add 3 numbers using append()
# Step3: Unpack into a, b, c using *
# Step4: Print numbers individually

# nums = []
# nums.append(int(input("Enter number 1: ")))
# nums.append(int(input("Enter number 2: ")))
# nums.append(int(input("Enter number 3: ")))
# a, b, c = nums
# print(a, b, c)


########################################################
# END OF EXERCISE SHEET — GREAT JOB! 🎯
########################################################
