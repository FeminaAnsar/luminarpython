//python dictionary
//javascript objects
var employee={
    id:1000,name:"ajay",desig:"designer",salary:25000
}
console.log(employee["id"]);
console.log(employee.name);
//check whether gender in employee
console.log("gender" in employee);
employee["gender"]="male"
console.log(employee);
for(item in employee)
{
    console.log(employee[item])
}