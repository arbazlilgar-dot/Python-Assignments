# Practical 10: Write a Python program to print custom exceptions.
# khud ki exception banayi


class MarksError(Exception):
    pass

try:
    marks = 150
    if marks > 100:
        raise MarksError("Marks 100 se zyada nahi ho sakte bhai!")
except MarksError as e:
    print("Custom Error Aaya:", e)