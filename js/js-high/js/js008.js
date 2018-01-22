Object.fun=function () {
    console.log("hello !");
}
Object.prototype.fun2=function () {
    console.log("hello !");
}
function Foo() {

}
console.log(Foo.__proto__);
console.log(Foo.__proto__.__proto__);
console.log(Object);
console.log(Foo.__proto__.__proto__==Object);
console.log(Foo.__proto__.__proto__==Object.prototype);
Foo.fun2();
var foo=new Foo();


function Foo2() {

}
var a={};
a.__proto__.fun=function () {
    console.log("hello 2");
}
Foo2.fun();
var foo2=new Foo2();
foo2.fun();
console.log([1,2,3]);