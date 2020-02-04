from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import  SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///myproject.sqlite3"

db=SQLAlchemy(app)


class Signup(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	s_name=db.Column(db.String(50))
	roll_no=db.Column(db.String(100))
	email_id=db.Column(db.String(150))
	phn_no=db.Column(db.String(200))
	branch=db.Column(db.String(150))
	def __init__(self,s_name,roll_no,email_id,phn_no,branch):
		self.s_name=s_name
		self.roll_no=roll_no
		self.email_id=email_id
		self.phn_no=phn_no
		self.branch=branch


@app.route('/myhtml/show')
def show():
	data=Signup.query.all()
	return render_template('showlist.html',data=data)



@app.route('/mypage/signup',methods=['POST','GET'])

def signup():
	if request.method == "POST":
		data=request.form
		s_name=data['sname']
		roll_no=data['rollno']
		email_id=data['email']
		phn_no=data['phnno']
		branch=data['branch']
		#print(s_name,roll_no,email_id,phn_no,branch)
		s=Signup(s_name,roll_no,email_id,phn_no,branch)
		db.session.add(s)
		db.session.commit()
		return render_template("details.html")

	return render_template("signup.html")








if __name__=='__main__':
	db.create_all()
	app.run(debug=True)