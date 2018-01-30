# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:26:43 2018

@author: Administrator
"""

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def singin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h1>hello,admin</h1>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
