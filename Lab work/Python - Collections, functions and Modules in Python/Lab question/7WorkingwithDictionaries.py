# 1. Write a Python program to update a value in a dictionary.
my_dict = {"name": "Arbaz", "age": 22}

# Updating the value of 'age'
my_dict["age"] = 23
print("Updated Dictionary:", my_dict)






# 2. Write a Python program to merge two lists into one dictionary using a loop.
keys_list = ["name", "age", "city"]
values_list = ["Arbaz", 23, "Ahmedabad"]

merged_dict = {}

# Merging using a for loop
for i in range(len(keys_list)):
    merged_dict[keys_list[i]] = values_list[i]

print("Merged Dictionary:", merged_dict)