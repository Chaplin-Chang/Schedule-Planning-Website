from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return "Index Page"
@app.route('/plusone/<int:num>')
def plusone(num):
	return "%d" % (num+1)
@app.route('/request', methods=['GET','POST'])
def processreq():
	if request.method == 'GET':
		return "Get key %s, val: %s" % (request.args.get('key'), request.args.get('val'))
	else:
		return "Post key %s, val: %s" % (request.form['key'],request.form['val'])
@app.route('/postpage/')
@app.route('/postpage/<pname>')
def postpage(pname="No name"):
	return render_template('postform.html', name=pname)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)