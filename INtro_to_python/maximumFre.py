s =input()
a ={}
for i in s:
    a[i] = a.get(i,0)+1
ct=0    
for i in a:
    ct = max(ct,a[i])
print(a)    
print(ct)