from flask import Flask,render_template
#from flask import bootstrap,Bootstrap
#from flask.ext.bootstrap import Bootstrap ----> This is old way of importing bootstrap from miguel videos. Below is upgraded way to import bootstrap
from flask_bootstrap import Bootstrap
from flask import request


app=Flask(__name__)
bootstrap = Bootstrap(app)

## Below if first loop that utilizes first.html page
@app.route('/',methods=['GET','POST'])
def disc():
    inputted_name=None
    if request.method == 'POST' and 'viname' in request.form:
        inputted_name=request.form['viname']
    return render_template('first.html',name=inputted_name)

if __name__ == '__main__':
    app.run(debug=True)