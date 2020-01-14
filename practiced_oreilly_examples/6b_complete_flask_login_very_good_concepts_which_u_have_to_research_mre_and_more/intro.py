from flask import Flask,render_template,redirect,request,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField,BooleanField,PasswordField
from wtforms.validators import Required,Length
from flask_sqlalchemy import SQLAlchemy ##### Database sqlalchemy wrapper plugin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,login_user,logout_user,UserMixin,login_required

app=Flask(__name__)
app.config['SECRET_KEY']='top secret'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://chintu:Saritha@123@192.168.209.171:3306/pdb'
bootstrap=Bootstrap(app)
dbconn=SQLAlchemy(app)
lm=LoginManager(app)
lm.login_view='login'

class LoginForm(Form):
    username=StringField("enter Username",validators=[Required(),Length(1,8)])
    password=PasswordField('password enter',validators=[Required()])
    remember_me=BooleanField('Remember me')
    submit=SubmitField('Click to submit here')

class User(UserMixin,dbconn.Model):
    __tablename__ = 'users'
    id=dbconn.Column(dbconn.Integer,primary_key=True)
    username=dbconn.Column(dbconn.String(16),index=True,unique=True)
    password_hash_stored=dbconn.Column(dbconn.String(128))

    def set_password(self,password):
        self.password_hash_stored=generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash_stored,password)
    
    @staticmethod
    def register(uname,password):
        user=User(username=uname)
        user.set_password('chintu')
        dbconn.session.add(user)
        dbconn.session.commit()
        return user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        #print('printing ------------------------------>')
        #print(user)
        #if user is None  or (not user.verify_password(form.password.data)):
        #if user and user.check_password(form.password.data): ---> This password check statement has error, so i validte only user as
        #if user is not None or user.password.check_password(form.password.data):
        if user is not None:
            login_user(user, form.remember_me.data)
            print('calling passed here')
            return redirect(request.args.get('next') or url_for('index'))
        else:
        #if user.verify_password(form.password.data):
        #if user.verify_password(form.password.data):
        #if (user is None) or (not user.verify_password(form.password.data)):
        #if user is None or not user.verify_password(form.password.data):
            #return redirect(url_for('login'))
            #return redirect(url_for('login', **request.args))
            return redirect(url_for('login'))
        
        # used for testing, print('Before hitting login screen')
        #login_user(user, form.remember_me.data)
        #print('calling passed here')
        #return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html',form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html') 

if __name__ == "__main__":
    dbconn.create_all()
    chk=User.query.filter_by(username='john').first()
    if not chk:
        User.register('john','cat')
    app.run(debug=True)
