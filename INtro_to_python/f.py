
def fun(a,n):
    for i in range (0,n-1,2):
        # temp= a[i]
        # a[i]=a[i+1]
        # a[i+1] =temp
        a[i],a[i+1] = a[i+1],a[i]
si = int(input('s'))       
print('enter the list')
a = [int(i) for i in input().split()]
fun(a,si)
print(a)
