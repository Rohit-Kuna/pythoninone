# Python Dictionary Practice Exercises - Follow Instructions
# Practice all dictionary operations and concepts 🧠🔥
# Focus on keys, values, immutability of keys, and performance benefits

########################################################
# 1️⃣ DICTIONARY CREATION
########################################################

# create an empty dictionary
d1 = 

# create dictionary with keys: name, age, city
d2 = 

# create dictionary using dict() converting list of pairs → [("a",1),("b",2)]
d3 = 

# create dictionary using comprehension
# keys: numbers 1 to 5, values: squares
# result: {1:1, 2:4, 3:9, ...}
d4 = 

########################################################
# 2️⃣ ACCESSING VALUES
########################################################

d_person = {"name": "Rohit", "age": 26, "role": "Developer"}

# access value of key "name"
name_val = 

# access key that doesn't exist using get() → default: "NA"
unknown_val = 

########################################################
# 3️⃣ ADDING & UPDATING
########################################################

# add new key-value pair: city="Hyd"

# update role to "Senior Developer"

# update multiple values at once using update()
# change city="Bangalore", add exp=3

########################################################
# 4️⃣ REMOVING ITEMS
########################################################

# pop value of key "role" and store in removed_role
removed_role = 

# remove last inserted item using popitem() → store in last_item
last_item = 

# use del to delete key "age"

########################################################
# 5️⃣ CHECKING MEMBERSHIP
########################################################

# check if key "city" exists → print Found/Not Found

########################################################
# 6️⃣ KEYS / VALUES / ITEMS
########################################################

info = {"a": 10, "b": 20, "c": 30}

# get keys in a variable → keys_var
keys_var = 

# convert keys to list → keys_list
keys_list = 

# get items → items_var
items_var = 

########################################################
# 7️⃣ COPY OPERATIONS
########################################################

# create shallow copy d5 of info
d5 = 

# modify d5 and check original remains unchanged

########################################################
# 8️⃣ NESTED DICTIONARY
########################################################

student = {
    "id": 101,
    "details": {"name": "Sam", "dept": "CSE"}
}

# access value "CSE" from nested dict → store in dept

########################################################
# 9️⃣ fromkeys() & CLEAR
########################################################

# create dict with keys ('x','y','z') each with default 0 → store in d6
d6 = 

# clear all elements of d6

########################################################
# 🔟 LENGTH, MIN, MAX, SUM on VALUES
########################################################

scores = {"math": 90, "science": 80, "english": 85}

# get length → total subjects
size = 

# get max score using max on values
max_score = 

# get min score using min on values
min_score = 

# get total score using sum on values
total_score = 

########################################################
# 1️⃣1️⃣ CONVERT BETWEEN DICT & LIST
########################################################

# convert keys of scores to list → scores_keys_list
scores_keys_list = 

# convert values of scores to tuple → scores_val_tuple
scores_val_tuple = 

########################################################
# 1️⃣2️⃣ BONUS CHALLENGES 💥
########################################################

# A) Merge two dicts using | operator (Python 3.9+)
a = {1:"A", 2:"B"}
b = {3:"C"}
# store merged dict in m
m = 

# B) Iterate over dictionary and print keys + values in format: key:value
# Example output: name:Rohit


# END OF EXERCISES 🎯 Good Luck!