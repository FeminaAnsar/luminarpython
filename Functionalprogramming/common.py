#print common elements from 2 lists
lst1=[2,4,6,8]
lst2=[1,2,3,4,5]
common=list(filter(lambda n:n in lst2,lst1))
print(common)
