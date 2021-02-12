class Stud:
    def __init__(self):
        print("no arg constructor")

    def __init__(self,name,age):
        print("two arg constructor")

obj1=Stud()
#obj1=Stud("tom",25)
#recently implemented constructor only works
#constructor overloading not works
