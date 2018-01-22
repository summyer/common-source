/**
 * Created by Administrator on 2017/4/25.
 */
//js原型与继承
/*(function () {
    function Person(name){
        this.name=name;
    }
    function PiTer(name,age){
        Person.call(this,name);
        this.age=age;
        this.getMessage=function () {
            return this.name+":"+this.age;
        }
    }
    PiTer.prototype=new Person();
    PiTer.prototype.constructor=PiTer;
    var p=new PiTer("sun","18");
    alert(p.getMessage());
})()*/

/*
function Father(name){
    this.name = name;
    this.colors = ["red","blue","green"];
    // this.sayName = function(){
    //     alert(this.name);
    // };
}
Father.prototype.sayName = function(){
    alert(this.name);
};
function Son(name,age){
    Father.call(this,name);//继承实例属性，第一次调用Father()
    this.age = age;
}
Son.prototype = new Father();//继承父类方法,第二次调用Father()
Son.prototype.sayAge = function(){
    alert(this.age);
}
var instance1 = new Son("louis",5);
instance1.colors.push("black");
console.log(instance1.colors);//"red,blue,green,black"
instance1.sayName();//louis
instance1.sayAge();//5
var instance1 = new Son("zhai",10);
console.log(instance1.colors);//"red,blue,green"
instance1.sayName();//zhai
instance1.sayAge();//10
    */

/*
function f(){
    if(this instanceof arguments.callee)
        console.log('此处作为构造函数被调用');
    else
        console.log('此处作为普通函数被调用');
}
f();//此处作为普通函数被调用
new f();//此处作为构造函数被调用*/
/*function f1() {

}
var temp = new f1();
f1. prototype = temp;
console.log(typeof temp);


var temp1 = new Function ();
Function.prototype = temp1;
console.log(typeof temp1);

console.log(typeof Function.prototype) // Function，这个特殊*/

function student() {


}
console.info(student.prototype.__proto__);
console.info(student.__proto__);
console.info(Function.__proto__);
console.info({}.__proto__);
console.info(Object.prototype);
console.info(Function.prototype);
console.info(Function.prototype.prototype);
console.info(student.prototype);