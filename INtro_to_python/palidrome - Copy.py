
n = input('enter rthe string')
x  = len(n)
flag = True
for i in range (0,x):
    if n[i] != n[x-i-1]:
        flag=False       
        break
    
if flag:
    print('palidrome')
else:
    print('not palidome')    

