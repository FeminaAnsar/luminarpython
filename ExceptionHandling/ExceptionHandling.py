#exception handling keywords
#try,except,finally
#try=>doubtful code in try block

num1=int(input("Num1:"))
num2=int(input("Num2:"))
try:
    res=num1/num2
    print("res=",res)
except Exception as e:
    print("Exception occured")
print("I have one database transaction")
print("I have file operations")