# Python Common Built‑in Functions - Complete Notes

# These functions work with iterables like: list, tuple, set, dictionary values
# They DO NOT modify the original iterable → always return a new value

########################################################
# 1️⃣ len() → find length of iterable
########################################################

nums = [10, 20, 30, 40]
length = len(nums)  # returns 4

########################################################
# 2️⃣ min() → minimum element in iterable
########################################################

values = [5, 9, 2, 7]
minimum = min(values)  # returns 2

# Works with strings too (based on alphabetical order)
min_char = min("hello")  # returns 'e'

########################################################
# 3️⃣ max() → maximum element in iterable
########################################################

maximum = max(values)  # returns 9
max_char = max("hello")  # returns 'o'

########################################################
# 4️⃣ sum() → sum of numeric elements
########################################################

# Parameters: iterable, start(optional default=0)
total = sum(values)  # returns 23

# Example with start value
extra_sum = sum(values, 10)  # returns 33 (10 + 23)

########################################################
# 5️⃣ sorted() → returns NEW sorted list
########################################################

nums2 = [4, 2, 8, 1]
sorted_list = sorted(nums2)       # ascending sorted list: [1,2,4,8]
sorted_desc = sorted(nums2, reverse=True)  # descending sort: [8,4,2,1]

# Does NOT change original list
# nums2 remains unchanged

########################################################
# 6️⃣ type() → tells data type
########################################################

type_of_nums = type(nums2)  # <class 'list'>

type_of_str = type("abc")  # <class 'str'>

########################################################
# 7️⃣ tuple(), list(), set() → type conversion
########################################################

my_tuple = tuple([1, 2, 3])  # Convert list to tuple
my_list = list((4, 5, 6))   # Convert tuple to list
my_set = set([1, 1, 2])     # Convert list → set removes duplicates

########################################################
# 8️⃣ any() → True if any element is True
########################################################

check_any = any([0, False, 5])  # returns True because 5 is True

########################################################
# 9️⃣ all() → True only if all elements are True
########################################################

check_all = all([1, True, 3])  # True
check_all2 = all([1, False, 3])  # False

########################################################
# 🔟 enumerate() → returns index and value pair
########################################################

fruits = ["apple", "banana", "mango"]
enum_fruits = list(enumerate(fruits))  # [(0,'apple'), (1,'banana'), (2,'mango')]

########################################################
# 1️⃣1️⃣ zip() → combine multiple iterables element‑wise
########################################################

names = ["A", "B", "C"]
scores = [90, 85, 88]
zipped = list(zip(names, scores))  # [('A',90), ('B',85), ('C',88)]

########################################################
# END OF NOTES
########################################################
