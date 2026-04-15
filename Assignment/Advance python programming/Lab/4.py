# Q.4 Write a Python program to read the contents of a file and print them on the console.
# 'r' mode se file read karenge


f = open("assignment.txt", "r")
data = f.read()
print("File data:\n", data)
f.close()