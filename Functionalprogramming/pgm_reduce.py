from functools import reduce

lst=[10,12,13,14,11]
sum=reduce(lambda no1,no2:no1+no2,lst)
print("Sum=",sum)
high=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(high)
low=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(low)
