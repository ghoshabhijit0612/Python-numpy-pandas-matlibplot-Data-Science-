class student:
    pass
s1= student()
s2 =student()
s3 = student()
s1.name = "abhi"
s1.age = 24
s2.roll = 23
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print(s1.name)