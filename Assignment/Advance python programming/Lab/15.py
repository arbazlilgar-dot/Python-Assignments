# Practical 5: Write a Python program to read a file and print the data on the console.

f = open("tops_assignment.txt", "r") # 'r' matlab read mode
file_data = f.read()
print("File ke andar likha hai:\n", file_data)
f.close()