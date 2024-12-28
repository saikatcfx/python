#wap t create non-peramiterised constructor
class Student():
    uni='rgu'
    def __init__(self,r,nam):
        self.roll=r       
        self.name=nam
    def display(self):    
        print(f'roll:{self.roll}  name:{self.name} university:{self.uni}')

      
   
roll=int(input("enter roll:"))
name=input("enter name:")
s1=Student(roll,name)
s2=Student(2,'asdf')
s1.display()
Student.display(s2)
print(s1.__dict__)  


print(s1.__dict__)







