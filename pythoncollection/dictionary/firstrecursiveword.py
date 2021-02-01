pattern="ABACBBAC"
#find first recursive char A
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,"is first recursive character")
        break