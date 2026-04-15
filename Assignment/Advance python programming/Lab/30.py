# Practical 20: Write a Python program to show method overriding.


class Developer:
    def code(self):
        print("Developer coding kar raha hai")

class PythonDeveloper(Developer):
    # Same function naam par naya logic likha (Override kiya)
    def code(self):
        print("Python Developer backend bana raha hai")

dev = PythonDeveloper()
dev.code() # Override hone ke baad naya wala chalega