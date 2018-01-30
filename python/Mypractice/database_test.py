# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:00:38 2018

@author: Administrator
"""
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#cursor.execute('insert into user(id,name) values (\'2\',\'sxk\')')
#print(cursor.rowcount)
cursor.execute('select * from user where id=?',('1',))
values=cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()

import mysql.connector
conn = mysql.connector.connect(user='root',password='123456',database='test')
cursor=conn.cursor()
cursor.execute('select * from person')
print(cursor.fetchall())
cursor.close()
conn.close()


from sqlalchemy import Column, String,Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    
    __tablename__ = 'person'
    
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
 
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

DBSession = sessionmaker(bind=engine)

session = DBSession()
person = Person(id=5,name='xs')
session.add(person)
person = session.query(Person).filter(Person.id==4).one()
print('name:%s,id:%s' % (person.name,person.id))
session.commit()
session.close()
    