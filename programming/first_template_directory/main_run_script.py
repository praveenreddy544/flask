from flask import Flask,render_template
app=Flask(__name__)

## Below if first loop that utilizes first.html page
@app.route('/')
def index():
    months=['January','February','March','April','May','June','July','August']
    return render_template('first.html', city='Chicago, IL', given_months=months)

## Below is loop that utilizes second.html loop
@app.route('/detailed_info')
def di():
    months=['January','February','March','April','May']
    weather= {
         'January':{'min':39,'max':42,'rain':6.14},
         'February':{'min':29,'max':32,'rain':5.14},
         'March':{'min':19,'max':49,'rain':4.14},
         'April':{'min':59,'max':22,'rain':5.14},
         'May':{'min':39,'max':42,'rain':6.14},
    }
    return render_template('second.html',city='Chicago, IL', given_months=months,weather_var=weather)

## Below is loop that utilizes third.html loop
@app.route('/desc')
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
    return render_template('third.html',city='Chicago, IL', given_months=months,weather_var=weather,highlight_this=highlight)

if __name__ == '__main__':
    app.run(debug=True)

