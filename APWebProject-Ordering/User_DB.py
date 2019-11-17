from flask import Flask, render_template, session, request, redirect, url_for
from flask.ext.pymongo import PyMongo
from passlib.hash import sha256_crypt
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

app = Flask(__name__)

app.config['DB_NAME'] = "Login"
#change the uri to whatever is true for us
app.config['DB_URI']= "mongodb://db1.example.net:27017,db2.example.net:2500/?replicaSet=test"

final_app= PyMongo(app)

@app.route('/')
def func1():
	if 'user_name' in session:
		return "Successsfully Logged In"

	#change argument value to whatever we have as index page
	return render_template('index.html')	

@app.route('/Login', methods= ["POST"])
def login():

	#this part is basically connection to the database
	#new_collection= MongoClient()["cakes"]["users"]
	#here we are gathering the user names and passwords
	#user_name = raw_input(" Enter Username: ")
	#password_val= raw_input(" Enter Password: ")
	
	user_name = final_app.db.cakes
	user_login= user_name.find_one({'Enter Username : ' : request.form['username'] })

	if user_login:
		if sha256_crypt.encrypt(request.form['pass'].encode('utf-8'), user_login['password'].encode('utf-8')) == user_login['password'].encode('utf-8')
		session['username'] = request.form['username']
		print ("Successsfully Logged In")
		return redirect(url_for('func1'))

	return "Incorrect Password/ Username. Try Again"	


@app.route() ('/register', methods=['POST','GET'])
def register:
	if request.method== 'POST':
		user_name = final_app.db.cakes
		alread_exists = user_name.find_one({'Enter Username : ' : request.form['username'] })

	if alread_exists is None:
		hash_password= sha256_crypt.encrypt(request.form['pass'].encode('utf-8'))
		user_name.insert({'Enter Username' : request.form['username'], 'Enter Password': hash_password})	
		session['username'] =request.form['username']
		return redirect(url_for('func1'))

	return 'User Already Exists'
		
#change page name to whatever our page is
return render_template('register.html')

	#hash_password= sha256_crypt.encrypt(password_val)
	#now we are trying to store them in our database
	#try : 
		#new_collection.insert({"_id": user_name, "password" : hash_password})
		#print ("Successsfully Added")
	#except DuplicateKeyError:
		#print ("User Already Exists")	




if __name__== '__main__':
	app.secret_key= 'mysecret'
	app.run(debug=True)