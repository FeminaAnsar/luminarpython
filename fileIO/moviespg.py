#yearwise number of movies released
#most number of movies released in year?
f=open("movies","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
for k,v in dict.items():
    print(k,":",v)
res=sorted(dict,key=dict.get,reverse=True)
print(res)
print("highest:",res[0],"with",dict.get(res[0]),"movies")
