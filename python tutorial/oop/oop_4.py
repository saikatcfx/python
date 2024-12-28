#wap to show setters 
class Student :
    def __init__(self):
        print("this is constructor")

    def setValues(self):
        self.name=input("enter your name:")
        self.age=int(input("enter your age"))
    
    def getValues(self):
        print(f'name : {self.name} age : {self.age}')


s1=Student()
s1.setValues()
s1.getValues()