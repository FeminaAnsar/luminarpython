

#print(sub(20,1000))
def subtract(func):
    def inner(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return func(num1,num2)
    return inner
@subtract
def sub(num1,num2):

    return num1-num2

data=sub(100,200)
print(data)
