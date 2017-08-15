from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('dojoSurvey.html')



@app.route('/dojo', methods=['POST'])
def dojoData():
    name = request.form['name']
    message = request.form['message']
    location = request.form['location']
    print name,message,location
    return render_template('submitted.html', name=name, message=message, location=location)


app.run(debug=True)
