from flask import Flask
simpleapp = Flask(__name__)
simpleapp.debug = True


@simpleapp.route('/')
@simpleapp.route('/data')

@simpleapp.route('/naveen/')
def chm():
  return "<h1>chm ---> chmm</h1>"

@simpleapp.route('/praveen/')
def index():
   #print(i)
   return 'chintu data is being held'

@simpleapp.route('/user/<int:id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)

if __name__ == "__main__":
#if __name__ == "__first__":
   simpleapp.run()
