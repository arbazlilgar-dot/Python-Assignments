# Q.3 Write a Python program to open a file in write mode, write some text, and then close it.
# 'w' mode se nayi file banegi aur write hoga


f = open("assignment.txt", "w")
f.write("This is my Advance Python lab assignment.")
f.close()
print("File successfully write ho gayi hai.")