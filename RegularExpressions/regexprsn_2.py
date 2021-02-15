from re import *
#pattern='[ab]'
#[] check for either a or b
#matcher=finditer(pattern,"abc _7ZK@c")
#for match in matcher:
 #   print(match.start())
  #  print(match.group())
#pattern='[0-9]'
#pattern='[^0-9]' #except 0-9 all elements will be printed
#check for lowercase a to z
pattern='[^a-zA-Z0-9]'
matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start())
    print(match.group())


