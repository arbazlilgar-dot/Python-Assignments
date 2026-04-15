# Q.7 Write a Python program to demonstrate handling multiple exceptions.


try:
    names = ["Arbaz", "Rehan", "Mohsin"]
    print(names[5]) # yaha index error aayega kyuki 5 items nahi hai
except ValueError:
    print("Value galat hai")
except IndexError:
    print("Error: List me itne item nahi hai")