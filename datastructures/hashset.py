hashset=set()

# add in hashset
hashset.add(10)
hashset.add(20)
hashset.add(30)
hashset.add(20)

size=len(hashset)

# check if an element exists in hashset i.e. 
# if hashset contains an element
if 20 in hashset:
    print("Exists")
else:
    print("Not Exists")
    
# remove from hashset
hashset.remove(20)
print(hashset)

# check if two sets are equal
s1=set([1,2,3])
s2=set([4,5,6])
s3={1,2,3}

if s1==s2:
    print("Equal")
else:
    print("Not Equal")

# iterate over set, remember the set is unordered
numset={21,56,42,21}
for x in s1:
    print(x)
    
# iterate over set and remove each element, and the set should be empty
# as set is unordered, we will iterate over the list copy of set, 
# atleast after modification the same element won't appear (as set when modified the elements can shift),
# using list we go over each element exactly once
for x in list(numset):
    numset.remove(x)
print(numset)