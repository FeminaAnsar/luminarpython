#class
#object
#reference
#class->plan,design,blueprint,template
#object->real world entity

class Person:
    #methods
    def setPerson(self,age,name):
        self.age=age
        self.name=name
    def printPerson(self):
        print("name=",self.name)
        print("age=",self.age)

obj=Person() #obj is reference -call class with class name

obj.setPerson("Ajay","25")
obj.printPerson()