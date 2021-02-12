#polymorphism
#more than one form
#method overloading
#method overriding
#operator overloading

#method overloading
class Maths:
    def add(self):
        print("inside no arg")

    def add(self,num1):
        print("inside one arg")

    def add(self,num1,num2):
        print("inside 2 arg")

m=Maths()
m.add(10)
#rcently implemented method is only invoked
