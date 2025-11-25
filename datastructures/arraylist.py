# array
arr=[]
arr=[1,2,30,4]

# append to an arraylist
arr.append(5)

# size
size=len(arr)

# access
arr[2]
arr[-1]

# search an element, get first occurrance
arr.index(30)

# remove an element's first occurrance
arr.remove(30)

# del or vacant a particular index so that everything else shifts to left
del arr[2]

# insert at particular index so that everything else after it is shifted to right
arr.insert(3,90)

# check equality of lists
# order matters
a=[1,2,3]
b=[2,3,1]
c=[1,2,3]
print(a==b)
print(a==c)

