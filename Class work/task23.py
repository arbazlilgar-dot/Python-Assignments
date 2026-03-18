x = 123
INT_MAX =  2147483647
INT_MIN =  -2147483648

is_nagetive = False
if x < 0 :
    is_nagetive = True
    x = x*-1

reversed_no = 0
while x > 0 :
    last_degit = x % 10 
    reversed_no = (reversed_no * 10) + last_degit
    x = x//10
if is_nagetive == True:
    reversed_no = reversed_no * -1

if reversed_no < INT_MIN or reversed_no > INT_MAX:
    print(0)

else:
    print(reversed_no) 