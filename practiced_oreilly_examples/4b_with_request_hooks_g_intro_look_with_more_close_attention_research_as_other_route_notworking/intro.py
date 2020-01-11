from flask import *
#import datetime
app=Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'

@app.before_request
def before_request():
    if not 'count' in session:
        session['count']=1
    else:
        session['count']+=1
    #g.when=datetime.now().strftime('%H:%M:%S')
    
@app.route('/')
def index():
    return render_template('index.html',count_value=session['count'])

@app.route('/other')
def other():
    #eturn "hello world"
    return render_template('call_other.html')
    #return render_template('oth.html',count_value=session['count'])

if __name__ == '__main__':
    app.run(debug=True)
