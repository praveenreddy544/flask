from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required,Length
from flask_sqlalchemy import SQLAlchemy ##### Database sqlalchemy wrapper plugin

app=Flask(__name__)
app.config['SECRET_KEY']='top secret'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://chintu:Saritha@123@192.168.209.162:3306/pdb'
bootstrap=Bootstrap(app)
dbconn=SQLAlchemy(app)
#print(f"Chintu you test is being executed")
 #### Python interpreter executes code base as per your statements

class NameForm(Form):
    inputted_name = StringField("whats your name", validators=[Required(),Length(1,8)])
    submitting = SubmitField('Submit here')

class CustomUserschintudefined(dbconn.Model): #### Define wahtever table name u want to as per your dbconn
    __tablename__= 'users'
    id = dbconn.Column(dbconn.Integer, primary_key=True)
    name = dbconn.Column(dbconn.String(16), index=True, unique=True)

    '''def __repr__(self):
        return '<User {0}>'.format(self.name)'''

@app.route('/',methods=['GET','POST'])
def index():
    name=None
    new=False

    form=NameForm()
    if form.validate_on_submit():
        name= form.inputted_name.data
        form.inputted_name.data = ''
        if CustomUserschintudefined.query.filter_by(name=name).first() is None:
             dbconn.session.add(CustomUserschintudefined(name=name))
             dbconn.session.commit()
             new = True
    return render_template('index.html',form=form,name=name,new=new)

if __name__ == "__main__":
    print(f"Chintu you test is being executed")
    dbconn.create_all() ##### This creates required table name called as users(you included in that) in provided database
    app.run(debug=True)

    