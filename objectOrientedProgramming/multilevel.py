class Parent:
    def m1(self):
        print("inside parent1")

class Child(Parent):
    def m2(self):
        print("inside child")

class Subchild(Child):
    def m3(self):
        print("inside sub child")
obj=Subchild()
obj.m3()
obj.m2()
obj.m1()
