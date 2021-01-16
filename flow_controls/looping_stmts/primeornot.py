num=int(input("Enter number to check prime or not:"))
flag=0
for i in range(2,num):
    print(i)
    if(num%i==0):
        flag=flag+1
        break
    else:
        pass
if(flag==0):
    print("Prime number")
else:
    print("Not prime")