class student:
    pass
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age
s1 = student("Abhiit",34,5)
print(s1.__dict__)        