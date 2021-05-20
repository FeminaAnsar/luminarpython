class Person{
    constructor(age,name){
        this.age=age
        this.name=name
    }
    printPerson(){
        console.log(this.name+ ","+this.age);
    }
}
//referencename=classname
var obj=new Person(25,"ajay")

obj.printPerson()
