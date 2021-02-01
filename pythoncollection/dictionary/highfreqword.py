pattern="ABACBBACEEEEEE"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
for key,value in dict.items():
    print(key,",",value)

print(dict) 
srtd=sorted(dict,key=dict.get)
print(srtd)
result=sorted(dict,key=dict.get,reverse=True)
print("Maximum occuring character",result[0])