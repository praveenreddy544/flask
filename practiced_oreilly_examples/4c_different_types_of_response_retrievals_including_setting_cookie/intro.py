from flask import Flask,render_template,make_response,jsonify,redirect,url_for
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text')
def text():
    return render_template('index.txt'), 200, {'Content-Type':'text/plain'}

@app.route('/xml')
def xml():
     return '<h1>this is shown as <b>XML</b> in the browser</h1>', 200, {'Content-Type':'application/xml'}

@app.route('/json')
def json():
    return jsonify({'firstname':'praveen','lastname':'reddy'})

@app.route('/redirect')
def red():
    return redirect(url_for('text')) ### This one is really useful if we want to have redirect feature in your app

@app.route('/error')
def error():
    return 'Page not there dear', 400

@app.route('/cookie')
def cookie():
    respnse=redirect(url_for('index'))
    respnse.set_cookie('idm','Hello dear chintu!')
    return respnse

@app.route('/responsiveness')
def responsiveness():
    rp=make_response(render_template('index.txt'))
    rp.headers['Content-Type'] = 'text/plain'
    return rp

if __name__ == "__main__":
    app.run(debug=True)