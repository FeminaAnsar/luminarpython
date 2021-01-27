lst=[10,11,12,13,14,15]
element=int(input("Enter element you want to search:"))
flag=0
count=1
for num in lst:
    if(element==num):
        flag+=1
        break
    else:
        pass
    count+=1
if flag==0:
    print("Element not found")
else:
    print("Element found at",count)