pragma solidity ^0.4.17;

contract Hello_mshk_top {
    mapping(uint=>uint) public balances;

  //say hello mshk.top
    function say() public  returns (string) {
        balances[1]=123;
        return "Hello mshk.top";
    }
   //print name
   function print(string name) public view returns (string,uint) {
	    return (name,balances[1]);
    }
    
    
}
