class Parent{
    m1()
    {
        console.log("inside parent classs");
    }

}
class Child extends Parent{
    m2(){
        console.log("inside child class");
    }
}
class SubChild extends Child{
    m3(){
        console.log("inside subchild class");
    }
}
var child=new SubChild()
child.m2();
child.m1();