employee={
    1000:{id:1000,"name":"tom","salary":25000,"exp":1},
    1001:{id:1001,"name":"john","salary":30000,"exp":2},
    1002:{id:1002,"name":"danie","salary":35000,"exp":2},
    1003:{id:1003,"name":"jack","salary":30000,"exp":2},
}
#nested dictionary
#print(employee[1000])#{id:1000,"name":"tom","salary":25000,"exp":1}
#print name of employee with id=1001
if 1001 in employee:
    print(employee[1001]["name"])
else:
    print("employee with id 1001 not exist")
    
if 1003 in employee:
    print(employee[1003]["salary"])
else:
    print("employee with id 1001 not exist")
