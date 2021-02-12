#constructor
#duty of constructor is initializing instnce variable
#constructor name always class name in java and cpp
#in python cnstrctr name is __init__()
#constructor automatically invoked during object creation
class Student:
    def __init__(self,rol,course,name):
        self.rol=rol
        self.course=course
        self.name=name
    def get_student(self):
        print(self.rol,",",self.course,",",self.name)

obj=Student(1001,"django","akhil")
obj.get_student()