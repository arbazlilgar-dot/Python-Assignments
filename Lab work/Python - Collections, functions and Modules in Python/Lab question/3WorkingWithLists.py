# 1. Write a Python program to iterate over a list using a for loop.
my_list = ["Apple", "Banana", "Cherry", "Mango"]

print("List elements are:")
for item in my_list:
    print(item)


# 2. Write a Python program to sort a list using both sort() and sorted().
my_list = [50, 10, 40, 20, 30]

# sorted() naya sorted list banata hai
new_sorted_list = sorted(my_list)
print("List using sorted():", new_sorted_list)

# sort() original list ko hi sort kar deta hai
my_list.sort()
print("List using sort():", my_list)