hm={}

# put in hm
hm[1]="A"
hm[2]="B"
hm[3]="C"

# remove from hashmap
del hm[3]

# if we want value returned we can use pop
hm.pop(2)

# if containsKey
if 1 in hm:
    print("Key Exists")
    
# same as
if 1 in hm.keys():
    print("Key Exists")
    
# get all keys
keyList=list(hm.keys())
valueList=list(hm.values())

# iterate over hm
for k,v in hm.items():
    print(str(k)+":"+v)
    
# frequency array
from collections import Counter
word="abbbabccd"
freq=Counter(word)

# check if two hashmaps are equal
s="java"
t="java"
hms=Counter(s)
hmt=Counter(t)

if hms==hmt:
    print("are anagrams")

# Iterate over dict and modify
# decrement the val, and remove a key if value is 0, finally the hm should be empty
freq = {"a": 4, "b": 0, "c": 5}

for key in list(freq.keys()):  # iterate over a copy of keys, as changing dict while iterating will cause runtime errors
    freq[key] -= 1  # decrement value

    if freq[key] <= 0:  # remove key if value <= 0
        del freq[key]

print(freq)
