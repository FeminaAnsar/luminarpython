class Parent:
    def m1(self):
        print("inside parent1")

class Child():
    def m1(self):
        print("inside child")

class Subchild(Child,Parent):
    def m3(self):
        print("inside sub child")
obj=Subchild()
obj.m3()
#obj.m2()
obj.m1()
#first check if there is m1 in subchild,then check for child .then parent(order of inherited classes)