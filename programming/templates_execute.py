from flask import Flask,render_template,request
#app=Flask(__name__,template_folder='templates')
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)

@app.route('/details/<id>')
def id_info(id):
    return render_template('id.html',sub_id_info=id)

if __name__ == '__main__':
    app.run(debug=True)