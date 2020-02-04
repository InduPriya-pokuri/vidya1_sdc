# import required Modules
from flask import Flask,render_template,url_for,request
from flask import redirect
from create_db import Base,User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

# Import required modules for Authentication
from flask import session as login_session
from functools import wraps

def required_login(f):
	@wraps(f)
	def x(*args,**wraps):
		if 'email' not in login_session:
			return redirect(url_for('login'))
		return f(*args,**wraps)
	return x

# Connect with already Existed Database
engine = create_engine('sqlite:///mydb.db')
Base.metadata.bind= engine
# create object for perform CRUD operations in database
session = scoped_session(sessionmaker(bind = engine))

# create Flask class object
app = Flask(__name__)

# c reate UR@app.route()L using route()
@app.route('/')
@app.route('/home')
def home():
	return "<h1>Welcome to Home Page.</h1><br>hi"

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method=="POST":
		email= request.form['emailid']
		password=request.form['password']
		login_user=session.query(User).filter_by(email=email,
			password=password).one_or_none()
		if not login_user==None:
			login_session['email']=email
			login_session['password']=password
			return "Successfully login"+email
		else:
			return "Enter Valid email & password"
	return render_template('login.html')

@app.route('/logout')
def logout():
	if 'email'in login_session:
		del login_session['email']
		del login_session['password']
		return "Logout Successfully"
	else:
		return "Please Login first"
		
@app.route('/register', methods=['GET','POST'])
def register():
	if request.method=="POST":
		name = request.form['username']
		password = request.form['password']
		email = request.form['emailid']
		mobile = request.form['Mobilenumber']
		new_user =User(name=name,
			email=email,
			password=password,
			mobile=mobile)
		session.add(new_user)
		session.commit()
		return "Successfully Inserted."
	else:
		return render_template('register.html')

@required_login
@app.route('/update/<email>',methods = ['GET','POST'])
def update(email):
	# fething record from db
	update_user =session.query(User).filter_by(email=email)\
											.one_or_none()
	#update_user=session.query(User).one_or_none()
	if request.method=='POST':
		update_user.name=request.form['username']
		update_user.password=request.form['password']
		update_user.mobile=request.form['Mobilenumber']
		session.add(update_user)
		session.commit()
		return "Successfully updated"+'---->'+update_user.email
	else:
		return render_template('update.html',update=update_user)

@required_login
@app.route('/display/<email>')
def display(email):
	display_user=session.query(User).filter_by(email=email)\
											.one_or_none()
	if not display_user==None:
		return render_template('display.html',user=display_user)
	else:
		return "Please Enter Existed Mail ID"+'.'*40

@app.route('/delete/<email>')
def delete(email):
	delete_user = session.query(User).filter_by(email=email)\
										.one_or_none()
	if not delete_user==None:
		session.delete(delete_user)
		session.commit()
		return "Record deleted Successfully."
	else:
		return "Please Enter Existed Mail ID"+'.'*40

@app.route("/home/<int:num>")
def number(num):
	return "number is " +str(num)

@app.route('/table/<int:value>')
def table(value):
	return render_template('table.html',value1=value)
# run flask server
# automatically update changes applyed when add "debug=True"

@app.route('/calculate/<int:a>/<int:b>/<string:op>')
def calculate(a,b,op):
	result=0
	if op=='+':
		result=a+b
	return str(result)
# @app.route('/image')
# def image():
# 	return render_template('demo.html')

app.secret_key="123456789"
app.run(debug=True)
