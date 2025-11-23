########################################################
# PYTHON STRINGS — EXERCISE SHEET
########################################################
# RULES OF STRINGS:
# - Strings are IMMUTABLE → cannot modify characters directly
# - Ordered sequence → supports indexing, slicing
########################################################



########################################################
# SECTION 1: STRING CREATION & BASIC ACCESS
########################################################

# TODO: Create a string s with value "Python Programming"
# s = "Python Programming"
# print(s)

# TODO: Access first character using index 0 → f_char
# f_char = s[0]
# print(f_char)

# TODO: Access last character using negative index → l_char
# l_char = s[-1]
# print(l_char)

# TODO: Slice substring "Python" from s → first_word
# first_word = s[:6]
# print(first_word)

# TODO: Reverse entire string using slicing → rev_s
# rev_s = s[::-1]
# print(rev_s)



########################################################
# SECTION 2: IMMUTABILITY TEST
########################################################

# TODO: Try modifying first character → write expected error in comment
# s[0] = 'J'  # ❌ TypeError: 'str' object does not support item assignment



########################################################
# SECTION 3: CONCATENATION & REPETITION
########################################################

greet = "Hello"
name = "Rohit"

# TODO: Concatenate greet and name with space using + operator
# full_msg = greet + " " + name
# print(full_msg)

# TODO: Repeat greet 3 times using * operator
# repeat_msg = greet * 3
# print(repeat_msg)



########################################################
# SECTION 4: SEARCHING & COUNTING
########################################################

text = "hello python hello"

# TODO: Count occurrences of "hello" using count()
# cnt_hello = text.count("hello")
# print(cnt_hello)

# TODO: Find index of "python" using index()
# idx_python = text.index("python")
# print(idx_python)



########################################################
# SECTION 5: PREFIX / SUFFIX CHECK
########################################################

# TODO: Check if text starts with "hello" using startswith()
# is_start = text.startswith("hello")
# print(is_start)

# TODO: Check if text ends with "python" using endswith()
# is_end = text.endswith("python")
# print(is_end)



########################################################
# SECTION 6: CASE CONVERSIONS
########################################################

msg = "heLLo WoRLd"

# TODO: Convert to UPPER case using upper()
# upper_msg = msg.upper()
# print(upper_msg)

# TODO: Convert to lower case using lower()
# lower_msg = msg.lower()
# print(lower_msg)

# TODO: Convert to title case using title()
# title_msg = msg.title()
# print(title_msg)

# TODO: Swap cases using swapcase()
# swap_msg = msg.swapcase()
# print(swap_msg)



########################################################
# SECTION 7: STRIP & REPLACE
########################################################

raw = "   Python   "

# TODO: Strip leading and trailing spaces using strip()
# strip_both = raw.strip()
# print(strip_both)

# TODO: Replace "Python" with "Java" using replace()
# replaced = raw.replace("Python", "Java")
# print(replaced)



########################################################
# SECTION 8: SPLIT & JOIN
########################################################

sentence = "a,b,c,d"

# TODO: Split by comma using split()
# parts = sentence.split(",")
# print(parts)

words = ["Python", "is", "awesome"]

# TODO: Join using space using join()
# joined = " ".join(words)
# print(joined)



########################################################
# SECTION 9: isX METHODS
########################################################

code = "Python3"

# TODO: Check if alphabetic (letters only) → isalpha()
# is_alpha = code.isalpha()
# print(is_alpha)

# TODO: Check if alphanumeric → isalnum()
# is_alnum = code.isalnum()
# print(is_alnum)

# TODO: Check if all uppercase → isupper()
# is_up = code.isupper()
# print(is_up)



########################################################
# SECTION 10: LENGTH, MIN, MAX
########################################################

# TODO: Find length of s using len()
# s_len = len(s)
# print(s_len)

# TODO: Find min character in "bca" using min()
# min_ch = min("bca")
# print(min_ch)

# TODO: Find max character in "bca" using max()
# max_ch = max("bca")
# print(max_ch)



########################################################
# SECTION 11: STRING FORMATTING
########################################################

lang = "Python"
level = "Beginner"

# TODO: Format using f-string → "Language: Python, Level: Beginner"
# f_str = f"Language: {lang}, Level: {level}"
# print(f_str)



########################################################
# SECTION 12: ESCAPE SEQUENCES
########################################################

# TODO: Create a string → He said, "Hello"
# esc_str = "He said, \"Hello\""
# print(esc_str)



########################################################
# BONUS CHALLENGE
########################################################

sent = "Python is easy and Python is powerful"

# TODO: Replace only first occurrence of "Python" with "Java"
# one_replace = sent.replace("Python", "Java", 1)
# print(one_replace)

# TODO: Remove ALL spaces using split + join → no_space
# no_space = "".join(sent.split())
# print(no_space)



########################################################
# END OF STRING EXERCISES — WELL DONE!
########################################################
