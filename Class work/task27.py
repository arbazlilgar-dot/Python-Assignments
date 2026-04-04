
def fac(n):
    if n==1:
      return 1

    else:
       return n*fac(n-1)
    
print(fac(5))


def prime(n, i=2):
   
   if n==i:
      return True
   
   elif n%i==0:
      return False
   return prime(n,i+1)

if prime(10):
   print("Yes Prime!!")

else:
   print("Not Prime!!")



