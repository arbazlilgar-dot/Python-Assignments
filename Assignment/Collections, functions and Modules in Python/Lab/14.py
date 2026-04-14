# Q.14 Write a Python program to merge two lists into one dictionary using a loop.
keys = ["name", "age", "city"]
values = ["Rehan", 21, "Ahmedabad"]
merged_dict = {}

# dono list ko loop chala ke ek me jod diya
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("Merged Dictionary:", merged_dict)