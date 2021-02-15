lst=[10,20,30]
pos=int(input("Enter the position to print element:"))

num1=int(input("Num1:"))
num2=int(input("Num2:"))
try:
    res = num1/num2
    print(res)
    print(lst[pos])
except Exception as e:
    print(e.args)