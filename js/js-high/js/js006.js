/**
 * Created by Administrator on 2017/4/26.
 */
function person(){
    this.name="sun";
}
function getCurrent(currentClass) {
    return new currentClass();
}
console.info(new person());
person.prototype.age="12";
console.info(person.prototype.age);
person.checkParam=function(){
    alert("a");
}
person.checkParam();

console.info(person.constructor);
console.info(typeof Object);
console.info(getCurrent(person).name);
console.info(getCurrent(person)["name"]);
console.info(getCurrent(person));

function student() {
    this.name="s";
}
student.prototype={
    age:23,
    sex:1
}
console.info(student.prototype);
/*
var name = 'zach'

while (true) {
    var name = 'obama'
    console.log(name)  //obama
    break
}

console.log(name)  //obama

console.log(1, 2)   //animal 2*/
