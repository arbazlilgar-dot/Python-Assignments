# 18) Write a Python program to count how many times each character appears in a string.
text = "hello"
count_dict = {}

for char in text:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print("Character count:", count_dict)