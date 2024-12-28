#wap t create default constructor
"""class Student():
    roll=1    # class variable
    name='hati'
    def display(self):
        print(f'roll:{self.roll} \t name:{self.name}')


s1=Student()
s2=Student()
s1.display()
Student.display(s1) 
"""

#wap t create non-peramiterised constructor
"""
class Student():
   
    def __init__(self):
        self.roll=int(input("enter your roll :"))
        self.name=input("enter name :")
    def display(self):    
        print(f'roll:{self.roll} \t name:{self.name}')


s1=Student()
s2=Student()
s1.display()
Student.display(s2)  """

#wap t create non-peramiterised constructor
"""
class Student():
   
    def __init__(self,r,nam):
        self.roll=r  #instance varibale
        self.name=nam
    def display(self):    
        print(f'roll:{self.roll} \t name:{self.name}')


roll=int(input("enter roll:"))

name=input("enter name:")

s1=Student(roll,name)
s2=Student(3,"java")
s1.display()
Student.display(s2)
print(s1.__dict__)
"""





