#mob no validation from file
from re import *
f=open("mobile_no","r")
word=[]
for lines in f:
    word.append(lines.rstrip("\n"))
print(lines)