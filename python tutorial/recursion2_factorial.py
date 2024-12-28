#wap to print factorial of this number:
def mul(n1):
     
     if(n1==1):
          return 1
     else:
        #   print(n1)
          return n1 * mul(n1-1)
          

n2=int(input("enter any number"))
sum=mul(n2)
print("total is",sum)


