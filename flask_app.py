#to delete files
import os, shutil, sqlite3

from copy import copy

#web application framework written in python
from flask import Flask, abort, session, request, url_for, make_response, redirect, render_template

# #to restrict types of files
# from werkzeug import secure_filename

# #personal python function that returns names, wikipedia summaries, and wikipedia links in documents
# from wikigrabber import gatherer as gr

# from articles import getArticles

# from dbfunc import dbcustomdata, dbinsert, dbquery, trymakeusertable, delete_entity_by_id, get_entity_name_by_id

# from summarizer import FrequencySummarizer 

# import nlp3

# from extractText import extractText

# from RAKE import rake


PRODUCTION = True
try:
	os.chdir('var/www/staketrak/staketrak')
except OSError:
	PRODUCTION = False

#define constants
UPLOAD_FOLDER = 'test_files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx', 'doc'])

MAX_SENT_PER_ENTITY = 10
MAX_TAGS_PER_ENTITY = 20
MAX_MENTIONS_PER_ENTITY = 20

# LOGINS = dbHandler.retrieveUsers()

#create a flask instance 
app = Flask(__name__)

# secret keyq
app.secret_key = '\xd3\xbdMBJ\xbb\xfe\x8d\xe4\xe9\xb8\x15\xde]\xd9ei\xfb\x8f1\xb2=O\x16'

#configure constant upload folder
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#render login
# @app.route('/', methods=['GET', 'POST'])
# def login():

# 	# if 'username' in session:
# 	# 	#trymakeusertable("db/" + session['username'] + ".db")
# 	# 	return redirect(url_for('index'))

# 	if request.method == 'GET':
# 		return render_template('login.html', error=0)
		
# 	if request.method == 'POST':
# 		LOGINS = dbHandler.retrieveUsers()
# 		if (not 'username' in request.form) or (not 'password' in request.form):
# 			# login failed - incomplete form
# 			return render_template('login.html', error=1)
		
# 		if request.form['username'] in LOGINS.keys():
# 			if request.form['password'] == LOGINS[request.form['username']]:
# 				session['username'] = request.form['username']
# 				return redirect(url_for('index'))
# 		else:
# 			# login failed - bad credentials
# 			return render_template('login.html', error="Account Does not Exist")
# 	else:
# 		abort(405)

# 	return redirect(url_for('index'))


# @app.route('/register', methods=['GET', 'POST'])
# def register():

# 	# if 'username' in session:
# 	# 	#trymakeusertable("db/" + session['username'] + ".db")
# 	# 	return redirect(url_for('index'))

# 	if request.method == 'GET':
# 		return render_template('register.html', error=0)
		
# 	if request.method == 'POST':


# 		# if (not 'username' in request.form) or (not 'password' in request.form):
# 		# 	# login failed - incomplete form
# 		# 	return render_template('login.html', error=1)
		
# 		# if request.form['username'] in LOGINS.keys():
# 		# 	if request.form['password'] == LOGINS[request.form['username']]:
# 		# 		session['username'] = request.form['username']
# 		# 		return redirect(url_for('index'))
		
# 		dbHandler.insertUser(request.form['username'], request.form['password'])
# 		return redirect(url_for('login'))


# 		# else:
# 		# 	# login failed - bad credentials
# 		# 	return render_template('login.html', error=2)
# 	else:
# 		abort(405)

# 	return redirect(url_for('login'))


#render homepage
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method=="GET":
		return render_template('index.html')
	else:
		return abort(404)


# @app.route('/step1', methods=['GET', 'POST'])
# def step1():
# 	if 'username' in session:
# 		# logged in!
# 		#print "RENDER_TEMPLATE:"
# 		#print render_template('index.html', username=session['username'])
# 		#print "USERNAME:"
# 		#print session['username']
# 		return render_template('step1.html', username=session['username'])
# 	else:
# 		return abort(404)

# @app.route('/step2', methods=['GET', 'POST'])
# def step2():
# 	if 'username' in session:
# 		# logged in!
# 		#print "RENDER_TEMPLATE:"
# 		#print render_template('index.html', username=session['username'])
# 		#print "USERNAME:"
# 		#print session['username']
# 		return render_template('step2.html', username=session['username'])
# 	else:
# 		return abort(404)

# @app.route('/step3', methods=['GET', 'POST'])
# def step3():
# 	if 'username' in session:
# 		# logged in!
# 		#print "RENDER_TEMPLATE:"
# 		#print render_template('index.html', username=session['username'])
# 		#print "USERNAME:"
# 		#print session['username']
# 		return render_template('step3.html', username=session['username'])
# 	else:
# 		return abort(404)

# @app.route('/step4', methods=['GET', 'POST'])
# def step4():
# 	if 'username' in session:
# 		# logged in!
# 		#print "RENDER_TEMPLATE:"
# 		#print render_template('index.html', username=session['username'])
# 		#print "USERNAME:"
# 		#print session['username']
# 		return render_template('step4.html', username=session['username'])
# 	else:
# 		return abort(404)

# @app.route('/step5', methods=['GET', 'POST'])
# def step5():
# 	if 'username' in session:
# 		# logged in!
# 		#print "RENDER_TEMPLATE:"
# 		#print render_template('index.html', username=session['username'])
# 		#print "USERNAME:"
# 		#print session['username']
# 		return render_template('step5.html', username=session['username'])
# 	else:
# 		return abort(404)


	
# @app.route("/logout", methods=['GET'])
# def logout():
# 	if not 'username' in session:
# 		return abort(404)
# 	if request.method == 'GET':
# 		if 'username' in session:
# 			session.pop('username', None)
# 	return redirect(url_for('login'))


#run app and use debugger to check Flask errors  
if __name__ == '__main__':
	app.run(debug = True)
