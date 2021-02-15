from re import *
#pattern a+ more than 1 number of a excluding 0 number of a
#pattern="a*" #any number of a  including 0 number of a
#pattern='a?' #occurance of single a including 0 number of a
#pattern="a{2}"#check for 2 number of a 's
pattern="a{2,4}"#max 4 min 2
matcher=finditer(pattern,"aaaaabaaaabaabbaabaaab")
for match in matcher:
    print(match.start(),"=>",match.group())