# 1. Write a Python program to update a list using insert() and append().
my_list = [10, 20, 30]

# append() se last mein add hota hai
my_list.append(40) 

# insert() se index 1 par 15 add hoga
my_list.insert(1, 15) 

print("Updated list:", my_list)


# 2. Write a Python program to remove elements from a list using pop() and remove().
my_list = [10, 20, 30, 40, 50]

# remove() se value 30 hategi
my_list.remove(30) 

# pop() se aakhri element hatega
my_list.pop() 

print("List after removal:", my_list)