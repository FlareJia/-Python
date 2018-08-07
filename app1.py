#-*- coding: utf-8 -*-
#app1.py
#用mvc模式改写
from flask import Flask, request, render_template

app1 = Flask(__name__)

@app1.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app1.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')

@app1.route('/signin', methods=['POST'])
def sigin():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == 'password':
		return render_template('signin-ok.html',username=username)
	return render_template('form.html', message='Bad username or password', username=username)
	
if __name__=='__main__':
	app1.run()