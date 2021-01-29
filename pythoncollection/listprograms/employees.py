employees=[
    [10,"Christy","dataanalyst",50000],
    [11,"john","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"johny","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000]
]

#print no of employees in this company
no_of_emp=len(employees)
print("Total number of employees :",no_of_emp)

#print how much salary cmpny has to raise in month end
total_amount=0
for emp in employees:
    total_amount+=emp[3]
print("Total amount :",total_amount)

#group by designation
dev_cnt,data_cnt,ba_cnt=0,0,0
for emp in employees:
    if emp[2]=="dataanalyst":
        data_cnt+=1
    elif emp[2]=="developer":
        dev_cnt+=1
    else:
        ba_cnt+=1
print("Number of developers :",dev_cnt)
print("Number of dataanalyst :",data_cnt)
print("Number of ba :",ba_cnt)

#print highest salaried employee
salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
high_salary=max(salary_list)
print("Highest salary:",high_salary)

for emp in employees:
    if emp[3]==high_salary:
        print(emp)

#print employee name who receives lowest salary whose desig=developer

low_salary=min(salary_list)
for emp in employees:
    if(emp[2]=="developer")&(emp[3]==low_salary):
        print("Employee with lowest salary:",emp)




