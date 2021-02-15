from re import *
#predefined character
#\s-space \d-digits \D-except digits \w-words except spl characetrs \W-except words print spl characters
pattern='\W'
matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start(),"=>",match.group())

