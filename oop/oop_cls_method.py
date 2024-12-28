# method in python ---/
#        class method
#        instance method
#        static method  


#insatance and class method
"""class  student:
    c_name='JBU'
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
    def display(self):
        print(f'your name:{self.name} your age:{self.age}')
    
    @classmethod  #decorator
    def change(cls):
        cls.c_name=input("enter clg name")

    

p1=student('joy',20)
print(p1.__dict__)

p1.display()
print(p1.c_name)


student.change()
print(student.c_name)"""



#satic method
class bank:
    rate=7.5
    
    @staticmethod
    def calulate(p,t): # p,t outside variable 
        si=(p*t*bank.rate)/100
        print(f'simple interset is {si}')
        

bob=bank()
bob.calulate(50000,60)


