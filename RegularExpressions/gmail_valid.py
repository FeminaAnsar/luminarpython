from re import *
f=open("Mail_id","r")
word=[]
valid_mail=[]
for lines in f:
    word.append(lines.rstrip("\n"))
for m in word:
    rule="[a-zA-Z0-9.]*@gmail.com"
    matcher=fullmatch(rule,m)
    if matcher ==None:
        pass
    else:
        valid_mail.append(m)
print("Valid Mail id:",valid_mail)
