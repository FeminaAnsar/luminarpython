#find even numbers from given list using list comprehension
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ls=[num for num in lst if(num%2==0)]
print(ls)