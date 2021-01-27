lst=[10,11,12,13,14,15,16,17]
lstodd=list()
lsteven=list()
for i in lst:
    if(i%2==0):
        lsteven.append(i)

    else:
        lstodd.append(i)
print("Even list :",lsteven)
print("Odd list :",lstodd)
print("Sum of odd list:",sum(lstodd))
print("Sum of even list:",sum(lsteven))
