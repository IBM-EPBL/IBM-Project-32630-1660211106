from flask import Flask,render_template
app = Flask(__name__)
@app.route("/department")
def  department():
	return render_template("department.html",tittle="HOME PAGE")
@app.route("/cse")
def cse():
	return render_template("cse.html",tittle="cse")
@app.route("/eee")
def  eee():
	return render_template("eee.html",tittle="eee")
@app.route("/it")
def  it():
	return render_template("it.html",tittle="it")

if
 __name__=="__main__":
	app.run(debug=True)