function person(name,age){
    this.name=name;
    this.age=age;
    this.colors = ["red","blue","green"];
}
function student(year,sex){
    this.year=year;
    this.sex=sex;
}
person.prototype.name="xia";
//student.prototype=person.prototype;
//person.prototype=null;
student.prototype=new person("xun","24");
var s=new student("1992","2");
var s1=new student("1992","33");
console.info(s);
console.info(s.colors);
console.info(s1.colors);
s.colors.push("black");
console.info(s.colors);
console.info(s1.colors);
console.info(s.__proto__);

console.info(s.constructor);

console.info(new person().constructor);


/*
//借用构造函数
//缺点：超类中定义的方法对子类不可见
function person(name,age){
    this.name=name;
    this.age=age;
}
function student(year,sex,name,age){
    this.year=year;
    this.sex=sex;
    person.call(this,name,age); //直接调用构造方法传入当前this执行，将person中的属性加入person
}
//person.prototype.name="xia";
//student.prototype=person.prototype;
//student.prototype=new person();
var s=new student("1992","2","sun","33");
console.info(s);
console.info(s.name);
console.info(s.__proto__);*/
