class Student:
    def set_student(self,rol,course,name):
        self.rol=rol
        self.course=course
        self.name=name
    def get_student(self):
        print(self.rol,",",self.course,",",self.name)

obj=Student()
obj.set_student(1001,"django","akhil")
obj.get_student()
print(obj.course)
print(obj.rol)

#set_student()
#initializeing instance variables
#instance variable(self. attached variables)
#we can access instance variables outside class by using reference

