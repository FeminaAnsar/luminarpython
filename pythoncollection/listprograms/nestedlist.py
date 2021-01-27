students=[
        [10,"Ajay","bca",250],
        [11,"Vijay","bca",240],
        [12,"Sibin","bca",220],
        [13,"Arun","mca",220],
        [14,"Abi","mca",180],
        [15,"Jain","mca",250]
]
#print(students)
#for student in students:
 #   print(student[1])

#print student names whose total>240

#for stud in students:
 #   if stud[3]>240:
  #      print(stud[1])

#print total sum of total
#marks=0
#for stud in students:
 #   marks+=stud[3]
#print("Total :",marks)

#calculate total of mca and bca separately
mtotal,btotal=0,0
for stud in students:
    if stud[2]=="bca":
        btotal+=stud[3]
    else :
        stud[2]=="mca"
        mtotal+=stud[3]
print("MCA total=",mtotal)
print("BCA total=",btotal)
