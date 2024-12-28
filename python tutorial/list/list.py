#list in python
# friends=["ram","shyam","jeet","joya","hati",5]
# print(friends[6])







#list program 2
# each and every items of a list is iterable
# friends=["ram","shyam","jeet","joya","hati",5]
# for i in friends:
#     print(i)











#list program 3
friends=["ram","shyam","jeet","joya","hati",5]
# for i in enumerate(friends): #enumeratr=index no. + list elemnt 
#     print(i)

    #   or
 


#      #variable
# for index,name in enumerate(friends):
#     print(index,name)





# list 4 program
# friends=["ram","shyam","jodu","modhu"]
# best_friend=friends[0]
# print("Best friend=",best_friend)

# best_friend,*other=friends
# print(other)







# #list 5 program
# friends1=["ram","shyam","tony","modhu"]
# friends2=["hati","goru","gadha"]

# all_friends=friends1+friends2
# print(all_friends)



# list 6 program wap to create a list using character list() method
# char_list=list("hello my world")
# print(char_list)


# list 7 program wap to count number of list item and print reverse list
#char_list=list("hello my world")
#total_chars=len(char_list)
#print(total_chars)

#print(char_list[::-1])


# # list 8 program wap to repulicate list item
# my_name=["ronojit "]
# names=my_name*12
# print(names)


#list 9 program
# my_numbers=list(range(11,21))
# print(my_numbers)


# print(my_numbers[5])            #16
# print(my_numbers[-4])           #len(my_numbers)-4=10-4=6=17
# print(my_numbers[1:5])          #[12,13,14,15]
# print(my_numbers[:4])           #[11,12,13,14]
# print(my_numbers[::2])          #[12,13,15,17,19]
# print(my_numbers[1::2])         #[12,14,16,18,20]
# print(my_numbers[::-1])         #step -1 to reverse ;ist=>[]




#list program 10
#wap to show different list functions
# my_subjects=["ram","shyam","jeet","joya","hati"]
# print(my_subjects)

# my_subjects.append("cs")
# print(my_subjects)

# my_subjects.insert(2,"phy")
# print(my_subjects)

# my_subjects.pop(3)
# print(my_subjects)










my_subjects=["ram","shyam","jeet","joya","hati"]
print(my_subjects)

try:
    sub=input("enter any string")
    idx=my_subjects.index(sub)
    my_subjects.pop(idx)
    print(my_subjects)

except:
    print("item not found")
#

my_subjects.remove("ram")
print(my_subjects)

del my_subjects[0:2]
print(my_subjects)

my_subjects.clear()
print("subjects are=",my_subjects)