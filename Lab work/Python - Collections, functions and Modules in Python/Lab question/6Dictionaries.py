# 1. Write a Python program to create a dictionary with 6 key-value pairs.
my_dict = {
    "name": "Arbaz",
    "age": 22,
    "course": "Python",
    "city": "Ahmedabad",
    "grade": "A",
    "status": "Active"
}
print("My Dictionary:", my_dict)



# 2. Write a Python program to access values using dictionary keys.
my_dict = {"name": "Arbaz", "course": "Python", "city": "Ahmedabad"}

# Accessing values using keys
print("Name:", my_dict["name"])
print("Course:", my_dict.get("course"))