from flask import Flask,render_template,request
import jsonify
import requests
import pickle
import numpy as np 
import sklearn


app = Flask(__name__)

model = pickle.load(open('car_price_prediction_model.pkl','rb'))

@app.route('/',methods = ['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        symboling = int(request.form['symboling'])
        curbweight = float(request.form['curbweight'])
        horsepower = float(request.form['horsepower'])
        citympg = float(request.form['citympg'])
        highwaympg = float(request.form['highwaympg'])
        enginesize = float(request.form['enginesize'])
        compressionratio = float(request.form['compressionratio'])
        peakrpm = float(request.form['peakrpm'])

        doornumber=request.form['doornumber']
        if(doornumber=='Two'):
            doornumber=2
        else:
            doornumber=4

        enginetype=request.form['enginetype']
        if(enginetype=='ohc'):
            enginetype=2 
        else:
            enginetype=1

        carbody=request.form['carbody']
        if(carbody=='Hatchback'):
            carbody=2
        elif(carbody=='Sedan'):
            carbody=3	
        elif(carbody=='Wagon'):
            carbody=4
        else:
            carbody=1

        drivewheel=request.form['drivewheel']
        if(drivewheel=='Read Wheel Drive'):
            drivewheel=1
        elif (drivewheel=='Front Wheel Drive'):
            drivewheel  = 2
        elif (drivewheel=='Four Wheel Drive'):
            drivewheel  = 3
        else:
            drivewheel= 0

        enginelocation=request.form['enginelocation']
        if(enginelocation=='Front'):
            enginelocation=1
        else:
            enginelocation  = 2

        cylindernumber=request.form['cylindernumber']
        if(cylindernumber=='Four'):
            cylindernumber= 4
        elif(cylindernumbe=='Six'):
            cylindernumbe = 6
        else:
            cylindernumbe  = 1
        

        fuelsystem=request.form['fuelsystem']
        if(fuelsystem =='mpfi'):
            fuelsystem= 1
        elif(fuelsystem =='2bbl'):
            fuelsystem = 2
        else:
            fuelsystem  = 0

        prediction=model.predict([[symboling,doornumber,carbody,drivewheel,enginelocation,curbweight,enginetype,cylindernumber,enginesize,fuelsystem,compressionratio,horsepower,peakrpm,citympg,highwaympg]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Cannot Find the Price")
        else:
            return render_template('index.html',prediction_text="Price of car is {} lakhs".format(output))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)





