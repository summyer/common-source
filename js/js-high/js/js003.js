function student(){
    this.name="sun";
    this.age="24";
}
student.prototype.name="d";
console.info(student.prototype);
console.info(student.prototype.name);

function person(){
    this.name="sun";
    this.age="24";
}
var p=new person();
console.info(p.name);
console.info(p.__proto__.name);