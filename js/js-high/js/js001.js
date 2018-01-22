/**
 * Created by Administrator on 2017/4/25.
 */
//js闭包的使用
var name="The window";
var object={
    name:"my object",
    getNameFunc:function () {
        return function () {
            return this.name;
        }
    }
};
alert(object.getNameFunc()());//The window

/*
var person="sun";
function hello(){
    var person="wang";
    alert(person);
    alert(this.person);
}
hello();*/


var person="sun";
function hello2(){
    var person="wang";
    alert(person);
    alert(this.person);
    function a() {
        alert(this.person);
    }
    return a;
}
hello2()();//wang sun sun