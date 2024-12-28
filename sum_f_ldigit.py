n=int(input("enter any number :"))
count=0
c=0#3241
while n!=0:
   if count==0:
      last=n%10
      count+=1
   rem=n%10
   n//=10

add=rem+last


print("Number of digits: ",add)