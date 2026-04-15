# Practical 6: Write a Python program to check the current position of the file cursor using tell().

f = open("tops_assignment.txt", "r")
print("Shuru me cursor position:", f.tell()) # start me 0 hoga

f.read(10) # 10 characters aage badha
print("10 character padhne ke baad cursor position:", f.tell())
f.close()