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
# #print(od)

# l = [1,2,3,4,5,1,2,3,4,]
# uni = []

# for i in l:
#    if i not in uni:
#        uni.append(i)
# print(uni)

# l = [11,2,3,2,11]

# left  = 0
# right = len(l)-1
# ans ="Yes"

# while (left<right):
#     if l[left]==l[right]:

#         left+=1
#         right-=1
#         continue
#     else:
#         ans = "No"
#         break
# print(ans)



bag = [10, 20, 10, 30, 20]
duplicate = [] # Ek nayi khali theli jisme hum answer rakhenge

for ball in bag:
    # Shart 1: Kya yeh ball bag mein 1 se zyada baar hai?
    # Shart 2: Kya maine isko pehle hi nayi theli (duplicate) mein daal diya hai?
    if bag.count(ball) > 1 and ball not in duplicate:
        
        duplicate.append(ball) # Agar dono shartein sahi hain, toh nayi theli mein daal do

print(duplicate)

