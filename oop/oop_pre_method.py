#wap to show the use of some predefined class method.
class person :
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag

p1=person('joy',20)
print(p1.__dict__)

# print(p1.name)
print(getattr(p1,'name')) #getattr(obj_name,'attribute_name) --- it is used to print object -- dictionary type 

# p1.name='prokash'
setattr(p1,'name','allu')   #setattr(obj-name,'attribute-name',)- to print changeing object name 
print(p1.__dict__)

# del p1.age
delattr(p1,'age')
print(p1.__dict__)


print(hasattr(p1,'age')) #show the current attribute preseny=t or not ?




