#mob no validation from file
from re import *
f=open("mobile_no","r")
word=[]
valid_mob=[]
for lines in f:
    word.append(lines.rstrip("\n"))
for mob in word:

    rule = "(91)?\d{10}"
    matcher = fullmatch(rule,mob)
    if matcher == None:
        pass
    else:
        valid_mob.append(mob)
print("Valid Mobile numbers:",valid_mob)