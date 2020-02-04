from flask import Flask,render_template,url_for,redirect


app=Flask(__name__)

@app.route('/myhome/<name>')
def home(name):
	return render_template('login.html',name1="sreevidya")

@app.route('/admin')
def admin():
	return "<h2>welcome admin</h2>"
@app.route('/librarian')
def librarian():
	return "<h2>welcome librarian</h2>"
@app.route('/student')
def student():
	return "<h2>welcome student</h2>"
@app.route('/user/<name>')
def user1(name):
	if name=='admin':
		return redirect(url_for('admin'))
	if name=='librarian':
		return redirect(url_for('librarian'))
	if name=='student':
		return redirect(url_for('student'))
@app.route('/myhtml/register')
def register():
	return render_template('registration.html')






if __name__=='__main__':
	app.run(debug=True)