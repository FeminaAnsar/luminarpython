#validate gmail
from re import *
mail=input("Enter gmail id:")
rule="[a-zA-Z0-9.]*@gmail.com"
matcher=fullmatch(rule,mail)
if matcher ==None:
    print("invalid gmail id")
else:
    print("Valid gmail id")