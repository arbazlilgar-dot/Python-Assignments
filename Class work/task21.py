#l = []

#ev = []
#od = []
#for i in range(1,31):
 #   l.append(i)
  #  if i%2==0:
 #       ev.append(i)

  #  else:
   #     od.append(i)

#print(i)
#print(ev)
#print(od)

#l = [1,2,3,4,5,5,4,2,2,6,1]
#uni = []

#for i in l:
 #   if i not in uni:
  #      uni.append(i)

l = [11,2,3,2,11]

left  = 0
right = len(l)-1
ans ="Yes"

while (left<right):
    if l[left]==l[right]:

        left+=1
        right-=1
        continue
    else:
        ans = "No"
        break
print(ans)

