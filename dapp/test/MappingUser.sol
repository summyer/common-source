pragma solidity ^0.4.17;

import {MappingExample} from './HelloWorld.sol';
contract MappingUser{
    
    address conAddr;
    address userAddr;
    
    function f() view returns (uint balance){
        conAddr = 0x93c1cda9befe914812012a09e7d7ae9a014ca77d;
        userAddr =0xe347a58750139a2af8992eff609c583314d3170b;
        return MappingExample(conAddr).balances(userAddr);
    }
}