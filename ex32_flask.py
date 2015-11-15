

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
	return '''
	<h1>Home page</h1>
	<p><button onclick = "location.href='/signin'">Sign In</button></p>
	'''


@app.route('/signin', methods = ['GET'])
def sigin_form():

	response = '''
	<form action = '/signin' method = 'post'>
	<p><input name = 'username'></p>
	<p><input name = 'password' type = 'password'></p>
	<p><button type = 'submit'>Sign In</button></p>'''
	return response

@app.route('/signin', methods = ['POST'])
def sigin():
	if request.form['username'] == 'admin' and request.form['password'] == 'password':
		return '''<h3>Hello, admin!</h3><p>
				<button onclick = "location.href='/signin'">back</button></p>'''

	return '''<h3>Bad username or password!</h3>
			<p><button onclick = "location.href='/signin'">back</button></p>'''

if __name__ == '__main__':
	app.run()
