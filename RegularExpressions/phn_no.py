#validate phone number
from re import *
reg_no=input("Enter Mobile number:")
rule="(91)?\d{10}"
matcher=fullmatch(rule,reg_no)
if matcher ==None:
    print("invalid Mobile number")
else:
    print("Valid Mobile number")