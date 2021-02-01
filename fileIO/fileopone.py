#read
#write
#append
#read file into progrm
#step 1: create reference
#f=open("filname","mode")

f=open("demotext","r")
word=[]
mywords=[]
for lines in f:
    word.append(lines.rstrip("\n").split(" "))
print(word)
for lst in word:
    for wrd in lst:
        mywords.append(wrd)
print(mywords)
