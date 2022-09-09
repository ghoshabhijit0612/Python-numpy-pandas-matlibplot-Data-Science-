def isprime(a):
    for i in range (2,a+1):
        if a%i==0:
            return False
    return True        

n = int(input('enter the number'))
x = isprime(n)
print(x)