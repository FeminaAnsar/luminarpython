#withdrawal-deposit-balance enquiry-create account
from datetime import datetime

class Bank:
    bank_name="sbi"
    def create_account(self,accno,personname,min_balanc):
        self.accno=accno
        self.p_name=personname
        self.balance=min_balance
       e
    def deposit(self,amount):
        self.balance+=amount
        print("Your account",self.accno,"has been credited with amt",amount,"on",datetime.today(),"avl bal",self.balance)
    def withdrawal(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print("Your account", self.accno, "has been debited with amt", amount, "on", datetime.today(), "avl bal",
                  self.balance)
        else:
            print("Transaction cancelled with error code")

    def balance_enq(self):
        print(self.balance)

obj=Bank()
obj.create_account(1000,"esther",3000)
obj.deposit(10000)