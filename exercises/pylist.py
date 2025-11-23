# RULES OF LISTS
# - Expressions do NOT modify the original list (they return new list)
# - If a method returns None → original list is modified
# - If a method returns something meaningful → original list is unchanged

########################################################
# 1️⃣ LIST CREATION & BASIC ACCESS
########################################################

# create an empty list
l0 = []  # O(1)
l0 = list()  # O(1)

# create a list with values 1 to 5 using []
num = [1,2,3,4,5]  # O(1)

# create a list with values using list(), passing an iterator in it
num = list()  # O(1)

# create a list of even numbers from 2 to 20
# 👉 Use list comprehension
l1 = [x for x in range(21) if x % 2 == 0]  # O(n)

# access element at index 3 and store in a variable named 'x'
x = l1[3]  # O(1)

# access last element from list
last = l1[-1]  # O(1)

# change value at index 2 to 20
l1[2] = 20  # O(1)


########################################################
# 2️⃣ ADD & REMOVE ELEMENTS
########################################################

# add 100 at the end of the list using append
l1.append(100)  # O(1) amortized

# add [200, 300] at end of list using extend
l1.extend([200,300])  # O(k) → k = new elements count → here O(2)

# insert 999 at index 1
l1.insert(1,999)  # O(n) (shifts all after elements to right)

# remove first occurrence of 8
l1.remove(8)  # O(n) (search + shift)

# remove element at index 4 using del keyword
del l1[4]  # O(n) (shifts all after elements to left)

# remove last element using pop()
removed_last = l1.pop()  # O(1)

# remove element at index 2 using pop()
removed_middle = l1.pop(2)  # O(n)


########################################################
# 3️⃣ SLICING PRACTICE
########################################################

# create a slice containing first 5 elements (store in new list slice1)
slice1 = l1[:6]  # O(k) → number of elements sliced

# create a slice of list containing first 6 elements but in reverse order using slicing
rev_slice = l1[6:-1:-1]  # O(k)

# delete a slice from index 1 to 3
del l1[1:4]  # O(n) (shifting elements)


########################################################
# 4️⃣ SEARCHING & COUNTING
########################################################

# check if 10 exists in the list using 'in'
if 10 in l1:  # O(n)
    print("Found")

# count number of occurrences of 4 using count()
count4 = l1.count(4)  # O(n)

# find index of first occurrence of 20 using index()
index20 = l1.index(20)  # O(n)


########################################################
# 5️⃣ COPYING LISTS
########################################################

# create a copy of the list using copy method
l2 = l1.copy()  # O(n)

# create copy using slicing
l3 = l1[:]  # O(n)


########################################################
# 6️⃣ ORDER OPERATIONS
########################################################

nums = [5, 2, 9, 1, 7]

# reverse nums list
nums.reverse()  # O(n)

# sort the nums list (ascending)
nums.sort()  # O(n log n)

# create a new sorted list from nums using sorted()
nums2 = [4,2,6,3,8]
sorted_nums = sorted(nums2)  # O(n log n)


########################################################
# 7️⃣ CONCATENATION & REPETITION
########################################################

l4 = [1, 2, 3]
l5 = [4, 5]

# concatenate l4 and l5 into l6 using '+' operator
l6 = l4 + l5  # O(n + m)

# create a list of five 0s using repetition operator
zeros = [0] * 5  # O(k)


########################################################
# 8️⃣ CLEAR DELETING LIST COMPLETELY
########################################################

# clear the list l5
l5.clear()  # O(n)

# delete entire list l6 using del
del l6[:]  # O(n)


########################################################
# 9️⃣ BONUS CHALLENGE 💥
########################################################

# remove ALL occurrences of 4 from l1
l1 = [x for x in l1 if x != 4]  # O(n) – best approach


########################################################
# 1️⃣2️⃣ PACKING AND UNPACKING 💥
########################################################

# 1️⃣ Unpack into variables
colors = ["red", "green", "blue"]
# TODO: unpack into c1, c2, c3 and print them
c1,c2,c3=colors
# print(c1, c2, c3)


# 2️⃣ Unpack with *
numbers = [10, 20, 30, 40, 50]
# TODO: unpack first two into n1, n2 and remaining into others
n1,n2,others=numbers
# print(n1, n2, others)


# 3️⃣ Swap variables using unpacking
a = 5
b = 10
# TODO: swap a & b
a,b=b,a
# print(a, b)

#############

# 4️⃣ Extract first and last name, rest in mid
names = ["Mr", "Rohit", "Kuna", "Fullstack", "Engineer"]
# TODO: title, first_name, *mid, last_name
title,first_name,*mid,last_name=names
# print(title, first_name, mid, last_name)


# 5️⃣ Extract first, middle(s), last
scores = [98, 85, 90, 92, 88]
# TODO: s1, *s_mid, s_last
s1,*s_mid,s_last=scores
# print(s1, s_mid, s_last)


# 6️⃣ Ignoring unwanted values
data = [101, "Laptop", 55000, "Electronics", "India"]
# TODO: extract id and price only (use _ for ignored ones)
id,_,price,*rest=data
# print(id, price)

############

# 7️⃣ Pack multiple variables into a list
x = "Python"
y = "Java"
z = "C++"
a = "JavaScript"
# TODO: langs = [...]
langs=[x,y,z,a]
# print(langs)


# 8️⃣ Combine lists using packing
list1 = [1, 2]
list2 = [3, 4]
# TODO: packed_list = [...]
packed_list=[*list1,*list2]
# print(packed_list)


print("\n=== Part 4: Unpacking in Functions ===")

# 9️⃣ Unpack while calling function
def display(a, b, c):
    print("Values:", a, b, c)

values = [100, 200, 300]
# TODO: call display using unpacking


# 🔟 Packing with *args inside function
# TODO: create function print_nums using *args
# Example call after writing:
# print_nums(10, 20, 30, 40)


print("\n=== Bonus Challenges ===")

# 11️⃣ Extract first, second-last, last
items = ["a", "b", "c", "d", "e", "f", "g"]
# TODO: unpack correctly
# print(first, second_last, last)


# 12️⃣ Merge 3 lists using unpacking
l1 = [1, 2]
l2 = [3, 4]
l3 = [5, 6]
# TODO: merged_list = [...]
# print(merged_list)


print("\n=== Final Exercise ===")

# 13️⃣ User input + packing + unpacking
# TODO:
# 1. Take 3 numbers from user
# 2. Pack into a list
# 3. Unpack and print individually

# Example:
# nums = []
# nums.append(int(input("Enter number 1: ")))
# ...
# a, b, c = nums
# print(a, b, c)

# END OF EXERCISE SHEET 🎯
########################################################
