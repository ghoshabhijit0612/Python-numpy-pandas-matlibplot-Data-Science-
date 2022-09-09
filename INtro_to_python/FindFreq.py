n=input()
a={}
for i in n:
    a[i] = a.get(i,0)+1
print(a)     