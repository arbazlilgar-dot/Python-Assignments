# Practical 9: Write a Python program to handle file exceptions and use the finally block for closing the file.


try:
    f = open("my_practical.txt", "r")
    print(f.read())
except IOError:
    print("File padhne me problem aayi.")
finally:
    # finally code hamesha execute hota hai, error aaye ya na aaye
    print("Main finally block hu, file close kar raha hu.")
    f.close()