#employee class
#eid,ename,desig,salary
#initialize
#print
#min 2 objcts
class Employee:
    def set_emp(self,e_id,e_name,desig,salary):
        self.e_id=e_id
        self.e_name=e_name
        self.desig=desig
        self.salary=salary
    def get_emp(self):
        print(self.e_id,"\t",self.e_name,"\t",self.desig,"\t",self.salary)

obj=Employee()
obj.set_emp(2002,"Anita","Developer",25000)
obj.get_emp()
obj1=Employee()
obj1.set_emp(2003,"Neethu","Testing",20000)
obj1.get_emp()