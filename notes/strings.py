# Python String - Complete Notes with Examples
# Strings are IMMUTABLE sequences of characters
# They support indexing, slicing, and many useful functions

########################################################
# 1️⃣ STRING CREATION
########################################################

s1 = "Hello"
s2 = 'Python'
s3 = ""  # empty string

# Multi-line string using triple quotes
s4 = """This is 
a multi-line string"""

########################################################
# 2️⃣ STRING INDEXING & SLICING
########################################################

text = "Python"
# Indexing (0-based)
first = text[0]       # 'P'
last = text[-1]       # 'n'

# Slicing: [start:end:step]
sub = text[1:4]       # 'yth'
rev = text[::-1]      # 'nohtyP'

########################################################
# 3️⃣ IMMUTABILITY
########################################################

# text[0] = 'J'  # ❌ TypeError → cannot modify
# Must create new string
new_text = 'J' + text[1:]

########################################################
# 4️⃣ STRING CONCAT & REPETITION
########################################################

sA = "Hello"
sB = "World"

greet = sA + " " + sB  # concat
repeat = sA * 3         # HelloHelloHello

########################################################
# 5️⃣ STRING MEMBERSHIP
########################################################

check = "Py" in "Python"  # True
not_check = "abc" in "Python"  # False

########################################################
# 6️⃣ STRING LOOPING
########################################################

for ch in "ABC":
    pass  # iterate character by character

########################################################
# 7️⃣ COMMON STRING METHODS
########################################################

# Case related
msg = "heLLo WoRLd"
upper = msg.upper()     # 'HELLO WORLD'
lower = msg.lower()     # 'hello world'
title = msg.title()     # 'Hello World'
capitalize = msg.capitalize()  # 'Hello world'
swap = msg.swapcase()   # 'HEllO wOrlD'

# Searching
text2 = "hello python hello"
count_h = text2.count("hello")     # 2
find_h = text2.find("python")      # index or -1
rfind_h = text2.rfind("hello")     # last index of match

# Checking prefix/suffix
starts = text2.startswith("hello")  # True
ends = text2.endswith("python")    # False

########################################################
# 8️⃣ STRIP & REPLACE
########################################################

raw = "   Python   "
strip1 = raw.strip()        # removes both sides
lstrip1 = raw.lstrip()      # removes left
rstrip1 = raw.rstrip()      # removes right

clean = text2.replace("hello", "hi")  # replace all

########################################################
# 9️⃣ SPLIT & JOIN
########################################################

sentence = "a,b,c"
parts = sentence.split(',')  # ['a', 'b', 'c']

words = ["Python", "is", "awesome"]
joined = " ".join(words)     # 'Python is awesome'

########################################################
# 🔟 IS-Checking Methods (Return True/False)
########################################################

s = "Python3"

isalpha = s.isalpha()  # False (contains number)
isdigit = s.isdigit()  # False
isalnum = s.isalnum()  # True
isupper = s.isupper()
islower = s.islower()
isspace = "   ".isspace()

########################################################
# 1️⃣1️⃣ STRING LENGTH & MIN/MAX
########################################################

length = len(text)  # number of characters
min_char = min("bca")  # 'a'
max_char = max("bca")  # 'c'

########################################################
# 1️⃣2️⃣ FORMAT STRINGS
########################################################

name = "Rohit"
age = 25

fmt1 = f"Name: {name}, Age: {age}"  # f-string
fmt2 = "Name: {} Age: {}".format(name, age)
fmt3 = "Name: {n} Age: {a}".format(n=name, a=age)

########################################################
# 1️⃣3️⃣ ESCAPE SEQUENCES
########################################################

esc = "Line1\nLine2"  # newline
quote = "He said, \"Hello\""  # escaping quotes

########################################################
# END OF STRING NOTES 🎯
########################################################
