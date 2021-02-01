text="hello hai hello hai hello"
#word_count
#hello:3 hai:2
words=text.split(" ")
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)