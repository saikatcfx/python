#user_define function 
#wap to print 1-10 using recursion
def mul(n1,n):
     
     if(n>10):
          return
     else:
          print(n1,"*",n,"=",n1*n)
          return mul(n1,n+1)
  
          
n1=int(input("enter any nymber:"))
mul(n1,1)

