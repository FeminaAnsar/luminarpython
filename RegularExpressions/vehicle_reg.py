#validate vehicle registration
#kl 2 digits 2 alphabets 4 digit
from re import *
reg_no=input("Enter Registration number:")
rule="kl\d{2}[a-zA-Z]{2}\d{4}"
matcher=fullmatch(rule,reg_no)
if matcher ==None:
    print("invalid Registration number")
else:
    print("Valid Registration number")