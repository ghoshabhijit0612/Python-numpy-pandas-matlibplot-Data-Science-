class student:
    pass
s1= student()
s2 =student()
s3 = student()
s1.name = "abhi"
s1.age = 24
s2.roll = 23
del(s1 ,'name')
print(s1.__dict__)