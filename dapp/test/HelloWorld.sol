pragma solidity ^0.4.0;

contract HelloWorld{
    uint balance;
    function update(uint amount) public returns (address,uint){
        balance += amount;
        return (msg.sender,balance);
    }
}
contract MappingExample{
    mapping(uint=>uint) public mapTest;
    mapping(address=>uint) public balances;
    function update(uint amount) public returns (address a){
        balances[msg.sender]=amount;
        mapTest[1]=amount;
        return msg.sender;
    }
    function getV(address v) public view returns (uint a,uint b,address ){
       // v=0xe347a58750139a2af8992eff609c583314d3170b;
        return  (balances[v], mapTest[1],v);
    }
}

