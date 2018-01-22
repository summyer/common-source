/*
console.log(foo);

function foo(){
    console.log("foo");
}

var foo = 1;
console.log(foo);*/

/*
console.log(foo);

function foo(){
    console.log("foo");
}
function foo(){
    console.log("foo change");
}
var foo = 1;

console.log(foo);*/

/*function foo() {
    console.log(a);
    a = 1;
}

foo();

function bar() {
    a = 1;
    console.log(a);
}
bar();*/

/*
console.info(a);
var a=3;
*/
/*

!function trigger() {
    var args = Array.prototype.slice.call(arguments);
    console.info(args);
    console.info(typeof args);
    console.info(arguments);
    console.info(typeof arguments);

}(1,2,3)*/

function fun(){
    console.info(this);
}
fun();