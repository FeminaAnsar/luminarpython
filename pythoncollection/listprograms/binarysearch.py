lst=[10,8,7,11,12,6,5]
lst.sort()
low=0
up=len(lst)-1
flag=0
element=int(input("Enter element for search:"))
while(low<=up):
    mid=(low+up)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        low=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if flag==0:
    print("Element not found")
else:
    print("Element found")
