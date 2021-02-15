num1=int(input("n1:"))
num2=int(input("n2:"))
try:
    res=num1/num2
    print(res)
except:
    num2=int(input("n2:"))
    try:
        res=num1/num2
        print(res)
    except Exception as e:
        num2=int(input("n2"))
        res=num1/num2
        print(res)
finally:
    print("I have database transaction")
    print("I have file operation")
