lst=["tcs","wipro","ae","klo","iop"]
cname=input("Enter company name:")
for comp in lst:
    if(comp==cname):

        flag+=1
        break
    else:
        flag=0
if flag==1:
    print("Found")
else:
    print("Not Found")
