l = [26,62,24,21,11,11]
uni = []
dup = []
checked = []

for i in l:
    if i not in uni:
        uni.append(i)

    else:
        dup.append(i)

print(uni)
print(dup)

if l.count(i) > 1 and i not in checked:
        print("Duplicate Value:", i)
        for index, val in enumerate(l):
            if val == i:
                print("Index:", index)
        checked.append(i)
