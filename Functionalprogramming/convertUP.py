names=["india","pak","aus","eng","sa","srilanka","aucklnd","indonasia"]
up_names=list(map(lambda name:name.upper(),names))
print(up_names)
#starting with a
acountry=list(filter(lambda name:name[0]=='a',names))
print(acountry)