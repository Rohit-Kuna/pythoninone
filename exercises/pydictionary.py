# Python Dictionary Practice Exercises - Follow Instructions
# Practice all dictionary operations and concepts 🧠🔥
# Focus on keys, values, immutability of keys, and performance benefits

########################################################
# 1️⃣ DICTIONARY CREATION
########################################################

# create an empty dictionary
d1 = {}

# create dictionary with keys: name, age, city
d2 = {
        "name":"RK",
        "age":24,
        "city":"Hyderabad"
    }

# create dictionary using dict() converting list of pairs → [("a",1),("b",2)]
d3 = dict([("name","Ryuzaki"),("age",20)])

# create dictionary using comprehension
# keys: numbers 1 to 5, values: squares
# result: {1:1, 2:4, 3:9, ...}
d4 = {x:x*x for x in range(6)}

########################################################
# 2️⃣ ACCESSING VALUES
########################################################

d_person = {"name": "Rohit", "age": 26, "role": "Developer"}

# access value of key "name"
name_val = d_person["name"]

# access key that doesn't exist using get() → default: "NA"
# unknown_val = d_person["unknown"] # KeyError: 'unknown'

########################################################
# 3️⃣ ADDING & UPDATING
########################################################

# add new key-value pair: city="Hyd"
d_person["city"]="Hyd"

# update role to "Senior Developer"
d_person["role"]="Senior Developer"

# update multiple values at once using update()
# change city="Bangalore", add exp=3
d_person.update({"city":"Bangalore","exp":3})
# hence update we can use to add new key or update an existing one

# add empId and try to use setdefault shouldn't change
d_person.setdefault("empId",101)
d_person.setdefault("empId",100001) # won't effect

########################################################
# 4️⃣ REMOVING ITEMS
########################################################

# pop value of key "role" and store in removed_role
removed_role = d_person.pop("exp")

# remove last inserted item using popitem() → store in last_item
last_item = d_person.popitem()

# use del to delete key "age"
del d_person["age"]

########################################################
# 5️⃣ CHECKING MEMBERSHIP
########################################################

# check if key "city" exists → print Found/Not Found
if "city" in d_person:
    print("Found")

########################################################
# 6️⃣ KEYS / VALUES / ITEMS
########################################################

info = {"a": 10, "b": 20, "c": 30}

# get keys in a variable using keys() → keys_var
keys_var = info.keys() # dict_keys(["a", "b", "c"])

# get items using values() → items_var
items_var = info.values() # dict_values([10,20,30])

########################################################
# 7️⃣ COPY OPERATIONS
########################################################

# create shallow copy d5 of info
info_copy = info.copy() # {"a": 10, "b": 20, "c": 30}

# modify d5 and check original remains unchanged
info.update({"d":40}) # {"a": 10, "b": 20, "c": 30, "d":40}
print(info_copy) # {"a": 10, "b": 20, "c": 30}

########################################################
# 8️⃣ NESTED DICTIONARY
########################################################

student = {
    "id": 101,
    "details": {"name": "Sam", "dept": "CSE"}
}

# access value "CSE" from nested dict → store in dept_val
dept_val=student["details"]["dept"]

########################################################
# 9️⃣ fromkeys() & CLEAR
########################################################

# create dict with keys ('x','y','z') each with default 0 → store in d6 using fromkeys()
# fromkeys() Creates a new dictionary from given keys and assigns a default value to all of them.
d6 = dict.fromkeys(["x","y","z"],0) # {'x': 0, 'y': 0, 'z': 0}

# clear all elements of d6
d6.clear()

########################################################
# 🔟 LENGTH, MIN, MAX, SUM on VALUES
########################################################

scores = {"math": 90, "science": 80, "english": 85}

# get length → total subjects
size = len(scores)

# get max score using max on values
max_score = max(scores.values())

# get min score using min on values
min_score = min(scores.values())

# get total score using sum on values
total_score = sum(scores.values())

########################################################
# 1️⃣1️⃣ CONVERT BETWEEN DICT & LIST
########################################################

# convert keys of scores to list → scores_keys_list
scores_keys_list = list(scores.keys())

# convert values of scores to tuple → scores_val_tuple
scores_val_tuple = list(scores.values())

########################################################
# 1️⃣2️⃣ BONUS CHALLENGES 💥
########################################################

# A) Merge two dicts using | operator (Python 3.9+)
a = {1:"A", 2:"B"}
b = {3:"C"}
# store merged dict in m
m = {**a, **b} # pythonic unpacking

# B) Iterate over dictionary d_person and print keys + values in format: key:value
# hint : use d.items() # dict_items([('name', 'Rohit'), ('age', 25)])
# Example output: name:Rohit
for k,v in d_person.items():
    print(k+":"+v)



# END OF EXERCISES 🎯 Good Luck!