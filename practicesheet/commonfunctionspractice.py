########################################################
# PYTHON BUILT-IN FUNCTIONS EXERCISE SHEET
########################################################
# Practice essential built-in functions for:
# len(), sum(), max(), min(), sorted(), any(), all(), type(),
# enumerate(), zip(), reversed()
########################################################



########################################################
# SECTION 1: BUILT-INS WITH LISTS
########################################################

L = [5, 2, 9, 1, 7]

# TODO: Find length of L using len()
# print(len(L))

# TODO: Find sum of all numbers using sum()
# print(sum(L))

# TODO: Get maximum number using max()
# print(max(L))

# TODO: Get minimum number using min()
# print(min(L))

# TODO: Create sorted copy of list using sorted()
# sorted_L = sorted(L)
# print(sorted_L)

# TODO: Check if any number > 8 exists using any() + comprehension
# exists = any(x > 8 for x in L)
# print(exists)

# TODO: Check if all numbers are positive using all()
# all_pos = all(x > 0 for x in L)
# print(all_pos)

# TODO: Print elements with index using enumerate()
# for idx, val in enumerate(L):
#     print(idx, val)

# TODO: Reverse list using reversed()
# rev_L = list(reversed(L))
# print(rev_L)

# TODO: Check datatype of L using type()
# print(type(L))



########################################################
# SECTION 2: BUILT-INS WITH TUPLES
########################################################

T = (10, 20, 5, 35)

# TODO: Find length of T using len()
# print(len(T))

# TODO: Find sum of values using sum()
# print(sum(T))

# TODO: Get max & min using max() and min()
# print(max(T))
# print(min(T))

# TODO: Convert reversed tuple into list using reversed()
# rev_T = list(reversed(T))
# print(rev_T)

# TODO: Check if any value < 0 using any()
# print(any(x < 0 for x in T))

# TODO: Sort tuple values into new list using sorted()
# sorted_T = sorted(T)
# print(sorted_T)



########################################################
# SECTION 3: BUILT-INS WITH SETS
########################################################

S = {4, 1, 7, 2}

# TODO: Find length of S using len()
# print(len(S))

# TODO: Find max & min using max() and min()
# print(max(S), min(S))

# TODO: Sort set into list using sorted()
# sorted_S = sorted(S)
# print(sorted_S)

# TODO: Check if all > 0 using all()
# print(all(x > 0 for x in S))

# TODO: Check if any even number exists using any()
# print(any(x % 2 == 0 for x in S))

# TODO: Print zipped pairs of S and list [10,20,30,40]
# Z = list(zip(S, [10,20,30,40]))
# print(Z)

# TODO: Reverse set elements → convert to list + reversed()
# rev_S = list(reversed(list(S)))
# print(rev_S)



########################################################
# SECTION 4: BUILT-INS WITH DICTIONARIES
########################################################

D = {"a": 100, "b": 50, "c": 150}

# TODO: Count number of key:value pairs using len()
# print(len(D))

# TODO: Find sum of values using sum()
# print(sum(D.values()))

# TODO: Get key with maximum value using max()
# max_k = max(D, key=D.get)
# print(max_k)

# TODO: Get key with minimum value using min()
# min_k = min(D, key=D.get)
# print(min_k)

# TODO: Get sorted list of keys using sorted()
# print(sorted(D.keys()))

# TODO: Check if any value > 100 using any()
# print(any(v > 100 for v in D.values()))

# TODO: Check if all keys are alphabetic using all()
# print(all(k.isalpha() for k in D.keys()))

# TODO: Loop using enumerate() → print index + key + value
# for idx, (k, v) in enumerate(D.items()):
#     print(idx, k, v)

# TODO: Reverse keys using reversed() + list()
# rev_keys = list(reversed(list(D.keys())))
# print(rev_keys)



########################################################
# BONUS SECTION: ZIP WITH MULTIPLE COLLECTIONS
########################################################

A = [1, 2, 3]
B = ("a", "b", "c")

# TODO: Zip together and convert to list → zipped_list
# zipped_list = list(zip(A, B))
# print(zipped_list)

# TODO: Unzip zipped_list back into separate values using *
# x_vals, y_vals = zip(*zipped_list)
# print(x_vals, y_vals)



########################################################
# END OF BUILT-IN FUNCTIONS EXERCISES — GREAT WORK!
########################################################
