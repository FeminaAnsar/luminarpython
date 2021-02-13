class Students:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name

obj=Students(100,"akshay","django",140)
obj1=Students(1001,"akhil","mean",140)
obj2=Students(1002,"ashik","django",145)

slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
tot=0
for stud in slist:
    #print(stud)
    if stud.course=="django":
        print(stud.name)
        tot+=stud.total
print(tot)
#print total of djago