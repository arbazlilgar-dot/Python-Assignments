# Q.5 Write a Python program to write multiple strings into a file.


f = open("multi_lines.txt", "w")
# list banayi strings ki
my_lines = ["Hello Sir\n", "This is line 2\n", "This is line 3\n"]
f.writelines(my_lines) # ek sath sab dal diya
f.close()