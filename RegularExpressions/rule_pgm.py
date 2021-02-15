#a,k first character must be an alphabet b/w a-k
#scond  must be a digit divisible by 3
#followed by any number of character
#z6kbb - not valid
#c8rtt-not valid
#a9bk-valid
from re import *
varname=input("Enter variable name:")
rule="[a-k][369][a-zA-Z0-9]*"
matcher=fullmatch(rule,varname)
if matcher ==None:
    print("invalid variable name")
else:
    print("Valid variable")
