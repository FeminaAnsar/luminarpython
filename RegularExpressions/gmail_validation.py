#validate gmail
from re import *
reg_no=input("Enter gmail id:")
rule="[a-zA-Z0-9.]*@gmail.com"
matcher=fullmatch(rule,reg_no)
if matcher ==None:
    print("invalid gmail id")
else:
    print("Valid gmail id")