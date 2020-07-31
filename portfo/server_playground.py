#flask is a framework/module for building servers
#the built in http.server is not recomended for production so choose something production ready

#a venv is recomended to use 
# python 3 comes with venv tool
# to create a venv : python -m venv <folder_name>
# i am using webserver as my venv folder
#command: python -m venv webserver run this in /webserver/.. directory
	
#once venv is installed we have to activate it by running activate file located in scripts of newly created venv
#this will bash us into venv that we created
#now whatever packages we install that will stay/used inside this env only
#now install flask  : pip install flask
#also run the python in this env only to make sure we are using proper libraries intended to use
from flask import Flask, render_template, request, redirect
import db_playground
app = Flask(__name__)

a_global_var = 'my name is baba :)'
# print(dir(app))
#to make sure when we start server this is the that runs we need to set environment variable FLASK_APP=<filename>.py
#on windows command to set env variable is: set FLASK_APP=server_playground.py
#to start server that we created just now run: flask run

#@app.route('urlpattern') is a decorator used to specify which function need to be executed when the url template is accessed
@app.route('/')
def my_home():
    return render_template('index.html')

#if we start server in debug mode it will notices the changes in FLASK_APP and hot reloads code on the server
#to enable debugger set env variable: set FLASK_ENV=development
#run the server :flask run

@app.route('/<string:page_name>')
def my_works(page_name):
    return render_template(page_name)

@app.route('/email_acknowledge',methods=['GET', 'POST'])
def email_sent():
	if request.method == 'POST' :
		data = request.form.to_dict()
		db_playground.write_to_csv([data['name'],data['subject'],data['message']])
		return redirect('/thankyou.html')
	return 'this is not what i am expecting from you :('

#to render html from a html file user render_template from flask
#Note the html file need to be in templates folder
#the other static files like .css,.js files need to be in static folder and the paths in html should refer with this directory
#we can read urlparams using <>
# @app.route('/home/<username>/<int:post_id>')
# def home_route(username='user',post_id=None):
# 	return render_template('index.html',name=username,post_id_t=post_id)