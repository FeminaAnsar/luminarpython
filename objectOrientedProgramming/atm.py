class Bank:
    def bal_enq(self):
        print("inside balance enq")
    def withdraw(self):
        print("inside withdraw")
    def __deposit(self):  #private method.call inside class with another public global method
        print("inside deposit")

obj=Bank()
#b.withdraw()
#b.mcall()
obj._Bank__deposit()