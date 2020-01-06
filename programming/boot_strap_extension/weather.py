from flask import Flask,render_template
#from flask import bootstrap,Bootstrap
from flask_bootstrap import Bootstrap
app=Flask(__name__)
bootstrap = Bootstrap(app)

## Below if first loop that utilizes first.html page
@app.route('/')
def disc():
    months=['January','February','March','April','May']
    weather= {
         'January':{'min':39,'max':42,'rain':6.14},
         'February':{'min':29,'max':32,'rain':5.14},
         'March':{'min':19,'max':49,'rain':4.14},
         'April':{'min':59,'max':22,'rain':5.14},
         'May':{'min':39,'max':42,'rain':6.14},
    }
    highlight={'min':25,'max':45,'rain':5}
    return render_template('index.html',city='Chicago, IL', months=months,weather=weather,highlight=highlight)

if __name__ == '__main__':
    app.run(debug=True)

