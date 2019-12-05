from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Chintu!</h1>"

@app.route('/user/<name>/')
def user(name):
    return "<h3>Hello, {0}!</h3>".format(name)

if __name__ == '__main__':
    app.run(debug=True)