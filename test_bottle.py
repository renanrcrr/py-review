from bottle import Bottle, run

app = Bottle()

msg = '''
<center><h1>Website</h1></center>
<p>Some description!<p>
<center><a href="/study_python">Click here to access the code library of Python</a></center>
'''

@app.route('/')
def index():
	return msg

@app.route('/study_python')
def studyPython():
	return '<center><h1>Welcome!! =) to the code library of Python</h1></center>\
			<center><a href="/">Go back to home page</a></center>'

run(app, host='localhost', port=8080)