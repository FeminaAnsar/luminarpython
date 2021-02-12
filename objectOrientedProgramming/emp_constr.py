class Employee:
    def __init__(self,e_id,e_name,desig):
        self.e_id=e_id
        self.e_name=e_name
        self.desig=desig

    def get_emp(self):
        print(self.e_id,"\t",self.e_name,"\t",self.desig)

obj=Employee(2002,"Anita","Developer")
obj.get_emp()
