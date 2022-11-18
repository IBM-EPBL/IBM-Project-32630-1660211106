import os
from flask import Flask
from flask import render_template,request,redirect,url_for,flash,session
import re
import os
from werkzeug.utils import secure_filename
from PIL import Image
from ml_model import food_identifier
from food import nutrients
import ibm_db
import json

app = Flask(__name__)
app.secret_key = 'a'

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rqn22933;PWD=v1K08EB1xJ6XXWmS",'','')


@app.route('/nutriCounter/login', methods =['GET', 'POST'])
def login():
	global id
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		sql = "SELECT * FROM accounts WHERE email = ? AND password = ? "
		stmt = ibm_db.prepare(conn,sql)
		ibm_db.bind_param(stmt,1,email)
		ibm_db.bind_param(stmt,2,password)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		if account:
            # Create session data, we can access this data in other route
			session['loggedin'] = True			
			session['id'] = request.form['email']
			session['email'] = request.form['email']
            # Redirect to home page
			return redirect(url_for('home'))
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/')
def home():
    # Check if user is loggedin
	login=False
	if 'loggedin' in session:
        # User is loggedin show them the home page
		# User is not loggedin redirect to login page
		login=True
		return render_template('home.html', username=session['email'], login=login)
	return render_template('home.html', login=login)
@app.route('/nutriCounter/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		sql = "SELECT * FROM accounts WHERE username = ?" 
		stmt = ibm_db.prepare(conn, sql)
		ibm_db.bind_param(stmt, 1, username)
		ibm_db.execute(stmt)
		account = ibm_db.fetch_assoc(stmt)
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			insert_sql = "INSERT INTO accounts(username, email,password) VALUES (?,?,?)"
			prep_stmt = ibm_db.prepare(conn, insert_sql)
			ibm_db.bind_param(prep_stmt, 1, username)
			ibm_db.bind_param(prep_stmt, 2, email)
			ibm_db.bind_param(prep_stmt, 3, password)
			ibm_db.execute(prep_stmt)
			msg = 'You have successfully registered !'
			# print(msg)
			return redirect(url_for('login'))
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)
if __name__ == "__main__":
    app.run(debug=True)
