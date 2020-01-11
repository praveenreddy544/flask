#from flask import Flask render_template,session
from flask import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'

@app.route('/')
def ind():
    if 'i' not in session: ### Session is similar to request which holds separate context for every client request
        session['i']=1
    else:
        session['i']+=1
    return render_template('index.html',count_value=session['i'])

if __name__ == '__main__':
    app.run(debug=True)