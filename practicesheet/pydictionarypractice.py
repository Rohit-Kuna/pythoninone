########################################################
# PYTHON DICTIONARIES — EXERCISE SHEET
########################################################
# RULES OF DICTIONARIES:
# - Key:Value pairs
# - Keys must be immutable (string, tuple, number)
# - No duplicate keys allowed → overrides previous value
# - Extremely fast access (hashing)
########################################################



########################################################
# SECTION 1: DICTIONARY CREATION
########################################################

# TODO: Create an empty dictionary using {}
# d1 = {}
# print(d1)

# TODO: Create dict d2 with keys name, age, city
# d2 = {"name": "RK", "age": 24, "city": "Hyderabad"}
# print(d2)

# TODO: Create dict d3 from list of tuples using dict()
# d3 = dict([("name", "Ryuzaki"), ("age", 20)])
# print(d3)

# TODO: Create dict comprehension mapping number to its square (1–5)
# d4 = {x: x*x for x in range(1, 6)}
# print(d4)



########################################################
# SECTION 2: ACCESSING VALUES
########################################################

d_person = {"name": "Rohit", "age": 26, "role": "Developer"}

# TODO: Get value of key "name" using []
# name_val = d_person["name"]
# print(name_val)

# TODO: Access missing key "unknown" using get() with default "NA"
# unknown_val = d_person.get("unknown", "NA")
# print(unknown_val)



########################################################
# SECTION 3: ADDING & UPDATING
########################################################

# TODO: Add new key "city" with value "Hyd" using assignment
# d_person["city"] = "Hyd"
# print(d_person)

# TODO: Update existing key "role" to "Senior Developer" using assignment
# d_person["role"] = "Senior Developer"
# print(d_person)

# TODO: Update multiple items using update()
# d_person.update({"city": "Bangalore", "exp": 3})
# print(d_person)

# TODO: Add key empId with value 101 using setdefault()
# d_person.setdefault("empId", 101)
# print(d_person)

# TODO: Call setdefault() on existing key empId with different value → no change
# d_person.setdefault("empId", 999)
# print(d_person)



########################################################
# SECTION 4: REMOVING ELEMENTS
########################################################

# TODO: Remove key "exp" using pop() and print removed + dict
# removed = d_person.pop("exp")
# print(removed, d_person)

# TODO: Remove last inserted item using popitem()
# last_item = d_person.popitem()
# print(last_item, d_person)

# TODO: Delete key "age" using del
# del d_person["age"]
# print(d_person)



########################################################
# SECTION 5: MEMBERSHIP TESTING (keys only)
########################################################

# TODO: Check if "city" exists in d_person using in
# if "city" in d_person:
#     print("Found")



########################################################
# SECTION 6: KEYS / VALUES / ITEMS
########################################################

info = {"a": 10, "b": 20, "c": 30}

# TODO: Store keys in keys_var using keys()
# keys_var = info.keys()
# print(keys_var)

# TODO: Store values in values_var using values()
# values_var = info.values()
# print(values_var)

# TODO: Get key-value pairs using items()
# items_var = info.items()
# print(items_var)



########################################################
# SECTION 7: COPY OPERATION (Shallow Copy)
########################################################

# TODO: Create copy of info using copy() → info_copy
# info_copy = info.copy()
# print(info_copy)

# TODO: Modify original info → prove copy unaffected
# info["d"] = 40
# print(info, info_copy)



########################################################
# SECTION 8: NESTED DICTIONARY ACCESS
########################################################

student = {
    "id": 101,
    "details": {"name": "Sam", "dept": "CSE"}
}

# TODO: Access "CSE" from nested dict
# dept_val = student["details"]["dept"]
# print(dept_val)



########################################################
# SECTION 9: fromkeys() & CLEAR
########################################################

# TODO: Create dict with keys x,y,z default value 0 using fromkeys()
# d6 = dict.fromkeys(["x", "y", "z"], 0)
# print(d6)

# TODO: Clear d6 using clear()
# d6.clear()
# print(d6)



########################################################
# SECTION 10: LENGTH, MIN, MAX, SUM ON VALUES
########################################################

scores = {"math": 90, "science": 80, "english": 85}

# TODO: Print number of subjects using len()
# print(len(scores))

# TODO: Print maximum score using max(values)
# print(max(scores.values()))

# TODO: Print minimum score using min(values)
# print(min(scores.values()))

# TODO: Print total score using sum(values)
# print(sum(scores.values()))



########################################################
# SECTION 11: TYPE CONVERSIONS
########################################################

# TODO: Convert keys of scores to list
# keys_list = list(scores.keys())
# print(keys_list)

# TODO: Convert values of scores to tuple
# vals_tuple = tuple(scores.values())
# print(vals_tuple)



########################################################
# SECTION 12: MERGING & ITERATION
########################################################

a = {1: "A", 2: "B"}
b = {3: "C"}

# TODO: Merge two dicts a and b using | operator (Python 3.9+)
# m = a | b
# print(m)

# TODO: Iterate d_person and print key:value pairs
# for k, v in d_person.items():
#     print(k, ":", v)

########################################################
# SECTION 13: PACKING & UNPACKING IN DICTIONARIES
########################################################
# Packing → Convert values into key:value structure
# Unpacking → Expand key:value pairs into another dict or function
########################################################


# TODO: Use unpacking (**) to merge two dictionaries into merged_dict
dA = {"id": 101, "name": "Alice"}
dB = {"dept": "IT", "location": "Hyderabad"}
# merged_dict = {**dA, **dB}
# print(merged_dict)


# TODO: Create dict d_pack using packing → assign multiple values via a dict literal
# d_pack = {"x": 10, "y": 20, "z": 30}
# print(d_pack)


# TODO: Use ** to unpack dictionary into function arguments
def display(id, name):
    print("ID:", id, "| Name:", name)

emp = {"id": 202, "name": "Bob"}
# display(**emp)   # unpack dictionary by key names


# TODO: Use dictionary comprehension with packing to create dict squares 1–5
# d_sq = {x: x*x for x in range(1, 6)}
# print(d_sq)


# TODO: Create a dict by unpacking list of tuples using dict()
# pairs = [("a", 1), ("b", 2)]
# d_from_list = dict(pairs)
# print(d_from_list)


# TODO: Unpack keys and values from dictionary into variables using *
# (keys list & values list)
D = {"p": 100, "q": 200, "r": 300}
# k1, k2, k3 = D   # unpack keys only
# print(k1, k2, k3)
# v1, v2, v3 = D.values()
# print(v1, v2, v3)


# TODO: Create new dict new_d using default values for missing keys during merge
defaults = {"role": "Developer", "active": True}
user = {"name": "Charlie"}
# new_d = {**defaults, **user}  # user overrides defaults
# print(new_d)


########################################################
# BONUS PACKING/UNPACKING PRACTICE
########################################################

# TODO: Convert tuple pairs → dict using unpack operator inside dict()
# tup_data = (("x", 1), ("y", 2))
# d_tup = dict(tup_data)
# print(d_tup)

# TODO: Expand dictionary into another using unpacking and add new key:value
# d_extended = {**D, "newKey": 400}
# print(d_extended)


########################################################
# END OF PACKING & UNPACKING FOR DICTIONARIES
########################################################



########################################################
# END OF DICTIONARY EXERCISES — GREAT WORK!
########################################################
