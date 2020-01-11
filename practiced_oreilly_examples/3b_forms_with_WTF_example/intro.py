from flask import Flask,render_template
#from flask import bootstrap,Bootstrap
#from flask.ext.bootstrap import Bootstrap ----> This is old way of importing bootstrap from miguel videos. Below is upgraded way to import bootstrap
from flask_bootstrap import Bootstrap
#from flask.ext.wtf import Form ---> old way of handling wtf
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required,Length

app=Flask(__name__)
app.config['SECRET_KEY'] = 'top sec'
bootstrap=Bootstrap(app)

class InjectForm(Form):
    #name=StringField("Whats your name?",validators=[Required(),Length(1,8)])
    name=StringField("Whats your name?",validators=[Required(),Length(1, 4)])
    submit=SubmitField('Submit here ana')
                                  
@app.route('/', methods=['GET','POST'])
def index():
    supplied_name=None
    inherit_form=InjectForm()
    if inherit_form.submit():
        supplied_name=inherit_form.name.data
        inherit_form.name.data=''
    return render_template('index.html',form=inherit_form,name=supplied_name)

if __name__ == '__main__':
    app.run(debug=True)

# reddyclik@gmail.com, saritha369

 