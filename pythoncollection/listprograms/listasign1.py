#q1
#input list=[2,6,8] output=[10,6,8]
#lst=[3,4,5] output=[9,8,7]

#lst=[2,5,6,7]
limit=int(input("Enter limit:"))
lst=list()
for i in range(0,limit):
    number=int(input("Enter number:"))
    lst.append(number)
#find total of list(20)
total=sum(lst)
out=list()
for num in lst:
    out.append(total-num)
print(out)

