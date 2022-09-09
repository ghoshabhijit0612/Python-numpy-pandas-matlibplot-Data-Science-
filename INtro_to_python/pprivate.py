class student:
    pass
    def __init__(self,name,roll,age):
        self.__name = 'abhi'
        self.roll = 12
        self.age = 20
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name    
s1 = student('abhi',34,56)
x = s1.getname()
s1.setname('alu')
print(s1.__dict__)