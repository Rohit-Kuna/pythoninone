d3 = dict([("name","Ryuzaki"),("age",20)])
print(d3.values())

print(d3.copy())

info = {"a": 10, "b": 20, "c": 30}



########################################################
# 7️⃣ COPY OPERATIONS
########################################################

# create shallow copy d5 of info
info_copy = info.copy() # {"a": 10, "b": 20, "c": 30}

# modify d5 and check original remains unchanged
info.update({"d":40})
print(info_copy)


student = {
    "id": 101,
    "details": {"name": "Sam", "dept": "CSE"}
}

# access value "CSE" from nested dict → store in dept
print(student["details"]["dept"])


scores = {"math": 90, "science": 80, "english": 85}

# get length → total subjects
size = len(scores)

# get max score using max on values
max_score = max(scores.values())
print(max_score)

a = {1:"A", 2:"B"}
b = {3:"C"}
# store merged dict in m
m = {**a, **b} # pythonic unpacking

print(m)