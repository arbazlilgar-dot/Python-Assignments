class A:
    def fun1(self):

        print("Method 1!!")

class B:

    def fun1(self):
         value =input("Enter value for reverse : ")
         print("Reverse value :",value[::-1])

class c(B,A):

    def fun1(self):
        super().fun1()
        value = input("Enter a string of number : ")
        if value == value[::-1]:
            print("it is a palindrome")
        else:
            print("it is not a palindrome")

obj = c()

obj.fun1()







