#regular expression
#step 1: import re module

from re import *

pattern="ab"
matcher=finditer(pattern,"abababbbbbabbbababababababb")
cnt=0

for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print("Count=",cnt)