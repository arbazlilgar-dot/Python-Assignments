# Q.6 Write a Python program to sort a list using both sort() and sorted().


marks = [45, 12, 89, 33]
new_sorted_marks = sorted(marks) # isse naya list banega, purana wesa hi rahega
print("Original after sorted():", marks)
print("New sorted list:", new_sorted_marks)

marks.sort() # isse original list hi change ho jayega
print("After sort():", marks)