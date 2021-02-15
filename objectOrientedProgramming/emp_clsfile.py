#print employee details whose designation is developer
#no of employees as developer
#print employee details with highest salary
class Employee:
    def __init__(self,eid,name,desig,exp,salary):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary
    def __str__(self):
        return self.name
f=open("employee_file","r")
emplist=[]
sallis=[]
dsal=[]
for lines in f:
    eid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(Employee(eid,name,desig,exp,salary))

#print employee details whose designation =developer
#devop=list(filter(lambda emp:emp.desig=="developer",emplist))
#for emp in devop:
 #   print(emp)

 #no of employees as developer

cnt=len(list(filter(lambda emp:emp.desig=="developer",emplist)))
print("No of developers:",cnt)

#print employee details with high sal
maxsal=max(list(map(lambda emp:emp.salary,emplist)))
print(maxsal)
for emp in emplist:
    if emp.salary==maxsal:
        print(emp.name)





#for employee in emplist:
 #   if employee.desig=="developer":
  #      print(employee.name)
   #     dsal.append(employee.salary)
#lowsal=min(dsal)
#for employee in emplist:
  #  if ((employee.desig=="developer")&(employee.salary==lowsal)):
   #     print(employee)
#for employee in emplist:
 #   sallis.append(employee.salary)
#print(max(sallis))
#highsal=max(sallis)

#for employee in emplist:
 #   if employee.salary==highsal:
  #      print(employee)

