# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:26:43 2018

@author: Administrator
"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def singin_form():
    return render_template("form.html")

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password',
                           username=username)


if __name__ == '__main__':
    app.run()
# -*- coding: utf-8 -*-

