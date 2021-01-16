num=int(input("Enter num:"))
lower=int(input("Enter lower:"))
upper=int(input("Enter upper:"))
for i in range(1,(upper+1)):
    if i**num in range(lower,upper):
        print(i**num)
    else:
        pass