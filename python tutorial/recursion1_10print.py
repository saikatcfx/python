
def mul(n1):
     
     if(n1==10):
          return 10
     else:
          print(n1)
          return n1 + mul(n1+1)
          

sum=mul(1)
print("total is",sum)