arr=[16,7,2,20,23]
size=5
flag=0
for i in range(0,size-1):
    for j in range(0,size-1-i):
        if(arr[j]> arr[j+1]):
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp

            flag=1

print(arr)


