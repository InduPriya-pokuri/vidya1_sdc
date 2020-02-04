from flask import Flask,render_template,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydata.sqlite3" # Connect the database

db = SQLAlchemy(app) 


class Sample(db.Model):

	id=db.Column(db.Integer,primary_key = True)
	name=db.Column(db.String(50))
	emailid=db.Column(db.String(100))
	Password=db.Column(db.String(150))
	Mobileno=db.Column(db.String(200))
	def __init__(self,name,emailid,Password,Mobileno):
		self.name=name
		self.emailid=emailid
		self.Password=Password
		self.Mobileno=Mobileno






@app.route('/myhtml/<name>')

def myhtml1(name):
	return render_template('sample.html',name1="sreevidya")


@app.route('/myhtml/show')
def show():
	data=Sample.query.all()
	return render_template('showlist.html',data=data)


@app.route('/myhtml/register',methods=['POST','GET'])
def register():
	if request.method == "POST":
		#data=request.form
		name=request.form['fname']
		emailid=request.form['email']
		Password=request.form['pswd']
		Mobileno=request.form['Mno']
		#print(name,emailid,Password,Mobileno)
		#flash("Successfully registered,you can login")
		#return render_template('login.html')
		sm=Sample(name,emailid,Password,Mobileno)
		db.session.add(sm)
		db.session.commit()
		return "<h1>Record stored</h1>"
		#print(data['fname'])
	flash("U Can Register Now")
	return render_template('register.html')
@app.route('/myhtml/login',methods=['POST','GET'])
def login():
	if request.method == "POST":
		Email=request.form['email']
		Password=request.form['pswd']
		#print(Email,Password)
	flash("you can register")
	return render_template('login.html')

if __name__=='__main__':
	app.secret_key = 'APP_SECRET_KEY'
	db.create_all()
	app.run(debug=True)