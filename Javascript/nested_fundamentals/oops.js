//class
//object
//reference

class Person{
    setPerson(age,name){
        this.age=age
        this.name=name
    }
    printPerson(){
        console.log(this.name+ ","+this.age);
    }
}
//referencename=classname
var obj=new Person()
obj.setPerson(25,"ajay")
obj.printPerson()