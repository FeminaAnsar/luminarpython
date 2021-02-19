from re import *
f=open("vehicle_regno","r")
word=[]
valid_reg=[]
for lines in f:
    word.append(lines.rstrip("\n"))
for m in word:
    rule="kl\d{2}[a-zA-Z]{2}\d{4}"
    matcher=fullmatch(rule,m)
    if matcher ==None:
        pass
    else:
        valid_reg.append(m)
print("Valid vehicle numbers:",valid_reg)