/**
 * ��ͨ�����Ժͺ���������������ϵ�?
 * ����̬�ĺ����Ƕ��嵽�������?
 */
(function(){
	function Person(name,age){
		this.name = name;
		this.showName = function(){
			alert(this.name)
		}
	}
	//��һ�־�̬������д��
	Person.add = function(x,y){
		return x+y;
	}
	//alert(Person.add(10,20))
	//�ڶ��ַ�ʽ
	//��������ķ�ʽ���ûһ������ȫӵ����ͬ�����ԺͲ���
	var cat = (function(){
		//˽�о�̬����
		var AGE = 10;
		var YEAR=[1];
		//˽�к���
		function add(x,y){
			return x+y;
		}
		return function(){
			this.AGE = AGE;
			this.YEAR=YEAR;
			/*this.add = function(x,y){
				return add(x,y)
			}*/
			this.add=add;
			this.setAge=function (age) {
				AGE=age;
			}
			this.setYear=function (year) {
				YEAR.push(year);
			}
		}
	})()
	/*var c1=new cat();
	var c2=new cat();
	alert(c1.YEAR);
	c1.setYear(15);
	alert(c1.YEAR);
	alert(c2.YEAR);*/
	var c=new cat();
	console.info(c.add(1,3));
	/**
	 * 1.�����ڲ������������Ƿ�װһ���ô�
	 * 2.������ع���ú�����,(���û�з�װ��ж���������Ĵ�����??)
	 * 3.����ģ��ֱ�ӵ����?
	 * �׶�
	 * ˽�еķ��������ú��ѽ��е�Ԫ����
	 * ʹ�÷�װ�ͻ���ζ���븴�ӵĴ���򽻵�?
	 * ��������Ƿ�װ��javascript���Ǻ���ʵ�ֵ�
	 */
})()
function a(a) {
	alert(a);
}
function a(a,b) {
	alert(a+b);
}
a(1);
a(1,3);


