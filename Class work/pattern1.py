#n = 5 

#for i in range(1, n + 1):         
 #   for j in range(1, i + 1):     
  #      print("*", end=" ")        
   # print()      



#n=6   
#for i in range (6,n-1):
 #   for j in range(6,i-1):
  #      print("*", end=" ")
   #     print()


for i in range (1,6):   #right angle 
    for j in range (1 , i+1):
        print("*", end=" ")
    print()

for i in range (1,6):  # lift angle  and space kar te hi triangle 
    for space in range(5 - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range (6,1):
    for j in range (6,i-1):
        print("*", end=" ")
    print()


#def fu1(n,n1,rev=0):    parameter
#print(n)
#print(rev)
#print(n1)


#fun1(1625,10) argument




def rev(n,rev1=0,rem=0):

    while(n>0):
        rem = n%10
        rev1 = rev1*10+rem
        n=n//10

    print(rev1)


n1 = int (input("Enter Number :"))
rev (n1)

def right(n):
    print("Right Angle Pattern:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

def left(n):
    print("Left Angle Pattern:")
    for i in range(1, n + 1):
        for space in range(n - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

rows = int(input("Enter Rows for patterns: "))
right(rows)
left(rows)