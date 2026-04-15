# Practical 4: Write a Python program to create a file and print the string into the file.


f = open("tops_assignment.txt", "w")
# directly text string ko print (write) kar rahe hai
text_string = "Advance Python Practical Assignment"
f.write(text_string)
f.close()