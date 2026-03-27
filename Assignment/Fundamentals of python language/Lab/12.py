# Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.

age = 22
weight = 55



if age >= 18:
    if weight >= 50:
        print("You can donate blood")
    else:
        print("Your weight is low for blood donate")
else:
    print("Your age is less to donate blood")