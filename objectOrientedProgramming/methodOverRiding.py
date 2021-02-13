class Parent:
    def mobile(self):
        print("nokia5310")
class Child(Parent):
    def mobile(self):
        print("Iphone11")


c=Child()
c.mobile()
# __str__(self) method that invoked when printing an object
#object class is base class for all classes
