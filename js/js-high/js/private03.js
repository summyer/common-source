/**
 * �հ�ʵ�ַ�װ
 */
(function(){
	function person(name,age,email,sex){
		this.email = email;//public ����
		//get
		this.getName = function(){
			return this.name;
		}
		this.getAge = function(){
			return this.age;
		}		
		//set
		this.setName = function(name){
			this.name = name
		}
		this.setAge = function(age){
			if(age>0 && age < 150){
				this.age = age
			}else{
				throw new Error("���������0��150֮��");
			}				
		}
		var _sex = "M";//��Ҳ��˽�б����ı�д��ʽ
		this.getSex = function(){
			return _sex;
		}
		this.setSex = function(){
			_sex = sex
		}
		/*this.init = function(){
			this.setName(name);
			this.setAge(age);
		}
		this.init();*/
		this.setName(name);
		this.setAge(age);
	}
	//ceshi 
	var p = new person("JIM",12,"www.USPCAT@126.COM")
})()




