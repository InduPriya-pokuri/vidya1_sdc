from flask import Flask,render_template,request


app=Flask(__name__)

'''@app.route('/')
def sample():
	return render_template('date.html')'''
@app.route('/myhtml',methods=['GET','POST'])
def details():
	if request.method=='POST':
		DOB=request.form['DOB']
		return render_template('submit.html',d=DOB)
	return render_template('details.html')




if __name__=='__main__':
	app.run(debug=True)