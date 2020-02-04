from flask import Flask,render_template

app=Flask(__name__)

@app.route('/mytable/<int:num>')

def table(num):
	return render_template('table.html',n=num)






if __name__=='__main__':
	app.run(debug=True)