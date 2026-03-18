d = {1:"hello",2:"python",3:"world",4:"hello1"}

print(d.get(1))             #get ye key jo nakho ge voh value print hoga 

print(d.items())            # sari value print ho ga 

print(d.keys())             # sari key print 

print(d.values())           # values print karata hai 

d.update({5:"why",6:"this"})
print(d)

d.pop(1)
print(d)

d.popitem()
print(d)