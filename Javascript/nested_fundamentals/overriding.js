class Parent{
    phone(){
        console.log("parent phone");
    }
}
class Child extends Parent{
    phone(){
        console.log("child phone");
    }
}
var ch=new Child()
ch.phone()
//class method
//object created by new
//self=>this
//constrctr creatd =>constructor
//inherited by extends
