from flask import Flask, render_template
app = Flask(__name__)
@app.route("/home")
def homepage():
	return render_template("home.html", title="HOME PAGE")
@app.route("/cse")
def cse():
	return render_template("cse.html", title="cse")
@app.route("/ece")
def ece():
	return render_template("ece.html", title="ece")
@app.route("/eee")
def eee():
	return render_template("eee.html", title="eee")
@app.route("/civil")
def civil():
	return render_template("civil.html", title="civil")
@app.route("/mech")
def mech():
	return render_template("mech.html", title="mech")
if __name__ == "__main__":
	app.run(debug=True)