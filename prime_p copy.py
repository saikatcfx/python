n=int(input("enter any number:"))
flag=0
for i in range(2,n//2):
    if(n%i==0):
        print("number not prime")
        flag+=1
        break 

if(flag==0):
     print(n,"is prime")

       
    
    
    
   
    