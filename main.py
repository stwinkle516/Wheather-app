from flask import Flask,render_template,request
import utils
app = Flask(__name__)

@app.route('/') #on calling this end point
def index():# this function will called
    return render_template("index.html")

@app.route("/getweather/",methods =["post"])
def getweather():
    form_data = dict(request.form)
    print(form_data)
    city = form_data["city"]
    
    res = utils.get_weather_data(city)
    return render_template("result.html", data=res )



@app.route("/add/<num1>/<num2>")
def get_add(num1,num2):
    addition=f"Addition of {num1}+{num2}={int(num1) + int(num2)} "
    return addition


app.run(debug=True)
