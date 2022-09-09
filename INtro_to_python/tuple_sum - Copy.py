# def sum(a,b,c=0,d=0):
#     return a+b+c+d
# n=sum(1,2)
# print(n)
def sum(a,b,*more):
    return a+b+more
x=sum(1,2,3,4,5,6,7)
print(x)    