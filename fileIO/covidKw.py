f=open("covid_19_India.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cured=data[6]
    death=data[7]
    confirmed=data[8]

    if state not in dict:
        dict[state]={"state":state,"cured":cured,"death":death,"confirmed":confirmed}
    else:
        dict[state]={"state":state,"cured":cured,"confirmed":confirmed}
print(dict)

def print_data(**kwargs):
    print(kwargs)
    state=kwargs["state"]
    if state in dict:
        print(dict[state]["state"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(dict[state][prop])
        else:
            pass
    else:
        print("state mentioned do not exist")
print_data(state="Kerala",prop="cured")
