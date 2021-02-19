def isRotation(a,b):
  flag=0
  if len(a) != len(b):
    flag=0
  a2=a*2
  i=0
  while(a[0]!=a2[i]):
      i+=1
  for x in a:
      if x!=a2[i]:
          f=0
      i+=1
  flag=1
  if flag==1:
        print("Rotation list")
  else:
        print("Not Rotation list")


lst1=[1,2,3,4,5,6]
lst2=[4,5,6,1,2]
print(lst1,lst2)
isRotation(lst1,lst2)



