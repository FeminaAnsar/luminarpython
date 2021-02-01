
#q2
#[1,2,3,4] i/p=6 o/p=[2,4]
lst=[1,2,3,4,5,6,7,8,9]
#um=int(input("Enter number to find pairs:"))
#for i in range(0,len(lst)):
  #  for j in range(i+1,len(lst)):
   #     if(lst[i]+lst[j]==num):
    #        print(lst[i],lst[j])
low=0
up=len(lst)-1
pair_list=[]
element=int(input("Enter element:"))
while(low<up):
    total=lst[low]+lst[up]
    if(element==total):
        pair_list.append((lst[low],lst[up]))
        up=up-1
    elif(element>total):
        low+=1
    else:
        up-=1
print(pair_list)

