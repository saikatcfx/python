#wap to single inhritance
'''
class Father:
    def __init__(self):
        self.car='Rolls royce'
        self.bank='10 cr'

class Son(Father):
    def showPop(self):
        print(f' car : {self.car} bank balance: {self.bank}')



joy=Son()
joy.showPop() '''
    
# wap to show single inhritance example 2
"""class Father:
    def __init__(self):
        self.car='Rolls royce'
        self.bank='10 cr'

class Son(Father):
    def __init__(self,laptop):
        super().__init__()
        self.laptop=laptop

    def showPop(self):
        print(f'  laptop : {self.laptop} car : {self.car} bank balance: {self.bank}')



joy=Son("avita")
joy.showPop()"""




#wap to show multilevel inheritance:
"""
class GrandFather:
    def __init__(self):
        self.car="rolls royce"
        self.bank='10 cr'

class Father(GrandFather):
    def __init__(self):
        super().__init__()
        self.flat='4cr'

class Son(Father):
    def __init__(self,laptop):
        super().__init__()
        self.laptop=laptop

    def showPop(self):
        print(f'  laptop : {self.laptop} car : {self.car} bank balance: {self.bank} flat: {self.flat}')


joy=Son("avita")
joy.showPop() """







#wap to show multilevel inheritance program 2:
"""class GrandFather:
    def __init__(self):
        self.car="rolls royce"
        self.bank='10 cr'

class Father(GrandFather):
    def __init__(self):
        super().__init__()
        self.flat='4cr'

class Son(Father):
    def __init__(self,laptop):
        super().__init__()
        self.laptop=laptop

    def showPop(self):
        print(f'  laptop : {self.laptop} car : {self.car} bank balance: {self.bank} flat: {self.flat}')


joy=Son("avita")
joy.showPop()"""


#wap to show multilevel inheritance program 3----------------------------------------------------------------------------------------------||
"""class GrandFather:
    def _init_(self, c, bk):  # Initializer for GrandFather
        self.car = c
        self.bank = bk

class Father(GrandFather):
    def _init(self, f, c, bk):  # Corrected the typo here: __init_ instead of init_
        super()._init_(c, bk)  # Call the GrandFather constructor
        self.flat = f

class Son(Father):
    def _init_(self, lptp, f, c, bk):  # Initialize Son with Laptop, Flat, Car, and Bank
        super()._init_(f, c, bk)  # Call the Father constructor
        self.laptop = lptp

    def showprop(self):
        print(f'Car: {self.car} Laptop: {self.laptop} Bank Balance: {self.bank} Flat valuation: {self.flat}')

# Creating an object of Son class
Prokash = Son('Avita', '15 cr.', 'Bugatti', '15cr')
Prokash.showprop()"""

''' GrandFather class initializes car and bank.
    Father class inherits from GrandFather and adds flat to the properties.
    Son class inherits from Father and adds laptop to the properties.
    The showprop() method in the Son class prints the values of all the properties inherited and defined in the class chain.'''



# wap to show hierarchical inheritance-------------------------------------------------------------------------------------------------------||
"""
class Father:
    def __init__(self):
        self.bank='10 cr'

class Son(Father):
    def __init__(self):
        super().__init__()
        self.car='BmW'

class Daughter(Father):
    def __init__(self):
        super().__init__()
        self.jewellery='dimond'

    # def showall(self):
    #     print(f' bank {self.bank} jelry {self.jewellery}')


s1=Son()
d1=Daughter()
print(s1.__dict__)
print(d1.__dict__)
d1.showall()
"""



#wap to show multilple inheritance-------------------------------------------------------------------------------------------------------------||
# class Father:
#     def __init__(self):
#         super().__init__()#default obj|| when we call super then this object call default obj ,then no object are presnt there it call Mother class throg inheritance 
#         self.bank='10 cr'

# class Mother:
#     def __init__(self):
#         self.glod='1kg'


# class Son(Father,Mother): #left side execute frist
#     def __init__(self):
#         super().__init__()
#         self.laptop='Asus'

# s1=Son()
# print(s1.__dict__)


##wap to show hybrid inheritance: ------------------------------------------------------------------------------------------------------------||
# class Grandparent:
#     def __init__(self):
       
#         self.bank='10 cr'

# class  Father(Grandparent):
#     def __init__(self):
#         super().__init__()
#         self.car='BmW'

# class  Mother(Grandparent):
#     def __init__(self):
#         super().__init__()
#         self.jewellery='dimond'


# class child(Father,Mother): #left side execute frist
#     def __init__(self):
#         super().__init__()
#         self.laptop='Asus'


# c1=child()
# print(c1.__dict__)

