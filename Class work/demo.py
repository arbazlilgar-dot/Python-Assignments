# l = [26,62,24,21,11,11]
# uni = []
# dup = []
# checked = []

# for i in l:
#     if i not in uni:
#         uni.append(i)

#     else:
#         dup.append(i)

# print(uni)
# print(dup)

# if l.count(i) > 1 and i not in checked:
#         print("Duplicate Value:", i)
#         for index, val in enumerate(l):
#             if val == i:
#                 print("Index:", index)
#         checked.append(i)



name = input("Enter Your name :")
marks = int(input("Enter your Total Marks : "))

if marks>=91 and marks<=100:
    print(name,"Your Grade is A")
elif marks>= 81 and marks<=90:
    print(name,"Your Grade is B")
elif marks>=71 and marks<=80:
    print(name,"Your Grade is C")
elif marks>=61 and marks<=70:
    print(name,"Your Grade is D")
elif marks<=60:
    print(name,"YOUR FAIL IN EXAM!!!")
else:
    print("Please enter valid number ")