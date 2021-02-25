num1=input("Enter a number:")
data=""
res=0
for i in range(1,(int(num1)+1)):
    data=num1*i
    print(data)
    res=res+int(data)
print("Result=",res)


