# 17) Write a Python program to convert two lists into one dictionary using a for loop.
keys = ["name", "age"]
values = ["Arbaz", 22]
my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("Dictionary from lists:", my_dict)