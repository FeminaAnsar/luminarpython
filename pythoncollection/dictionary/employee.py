employ={"id":100,"ename":"ajay","salary":35000}
if("salary" in employ):
    print(employ["salary"])
print(employ["ename"])
if("gender" in employ):
    print("exit")
else:
    employ["gender"]="male"
print(employ)

#if employ salary less than 35000 add 5000
if(employ["salary"]<=35000):
    employ["salary"]+=5000

print(employ)