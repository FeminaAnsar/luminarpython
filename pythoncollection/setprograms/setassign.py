students=["hari","nithin","vega","esther","sneha","hari"]
fail1=["vega","nithin"]
studset=set(students)
failset=set(fail1)
pas=studset.difference(failset)
pas_list=list(pas)
print("passed students:",pas_list)