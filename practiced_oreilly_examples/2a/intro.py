from flask import Flask,render_template
simpleapp = Flask(__name__)
simpleapp.debug = True

@simpleapp.route('/')
def index():
    return render_template('index.html')

@simpleapp.route('/details/<username>/')
def ind(username):
    return render_template('user.html',name=username)

@simpleapp.route('/user/<username>/')
def user(username):
    return "Profile page is for {}".format(username)

if __name__ == "__main__":
#if __name__ == "__first__":
   simpleapp.run()