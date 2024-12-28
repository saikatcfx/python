#wap to enter 1st and last no  from the user and create a list
# wap to input a list using split method 
# f=int(input("enter 1st no"))
# l=int(input("enter 1st no"))

p=0
n=list(input("enter any sentence:"))
total_char=len(n)
i=0
while(i<total_char):
    if(total_char ==''):
     p+=1
   

print(p)

my_sentence=input("enter any sentence").split()
print("total no word ",len(my_sentence))

# list_between=(range(f,l+1))
# print(list_between)

# # wap to input a list using split method 
# my_number=input("enter the numbrrs").split(',')
# print("list created\nlist element\t",my_number)

