from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/mydata/register",methods=['POST','GET'])

def register():
	if request.method == "POST":
		name=request.form['fname']
		emailid=request.form['email']
		Password=request.form['pswd']
		Mobileno=request.form['Mno']
		#print(name,emailid,Password,Mobileno)
		#flash("Successfully registered,you can login")
		return render_template('display.html',n=name,e=emailid,p=Password,m=Mobileno)
	#flash("U Can Register Now")
	return render_template('register.html')
		#return render_template('display.html')





if __name__=='__main__':
	app.run(debug=True)