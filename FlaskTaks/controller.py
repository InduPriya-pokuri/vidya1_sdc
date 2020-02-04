from flask import Flask,redirect,url_for

app=Flask(__name__)

#Flask environment exmaple and how to create a routing in flask
@app.route('/')
def home():
	return render_template("table.html")

'''#App Routing
@app.route('/home')
def home():
	return "<h2>Hello World</h2>"'''


'''#Adding the variable
@app.route('/home/<name>')
def home(name):
	return "welcome "+name'''


'''#adding age
@app.route('/home/<int:age>')
def home(age):
	return "age=%d"%age'''

'''def about():
	return "this is about page "
app.add_url_rule("/about","about",about)'''
'''# URl Building
@app.route('/admin')
def admin():
	return "welcome admin"
@app.route('/librarion')
def librarian():
	return "welcome librarian"
@app.route('/student')
def student():
	return "welcome student"
@app.route('/user/<name>')
def user(name):
	if name=='admin':
		return redirect(url_for('admin'))
	if name=='librarian':
		return redirect(url_for('librarian'))
	if name=='student':
		return redirect(url_for('student'))'''





if __name__=='__main__':
	app.run(debug=True)