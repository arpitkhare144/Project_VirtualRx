import cluster as cluster
import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request
import pandas as pd
import os
from datetime import datetime

now = datetime.now() # current date and time
today=now.strftime("%m/%d/%Y")
print(today)
app = Flask(__name__)

cluster = MongoClient("mongodb+srv://arpit:567arpit@cluster0.ot8xk.mongodb.net/rx?retryWrites=true&w=majority")
db = cluster["rx"]








collection=db["prescription"]
x=collection.find_one({"date":"03/09/2021"})
print(x)
date=x.get("date")
dname=x.get("dname")
pname=x.get("pname")
padhar=x.get("padhar")
page=x.get("page")
roomtemp=x.get("roomtemp")
heartrate=x.get("heartrate")
bodytemp=x.get("bodytemp")
opd=x.get("opd")
roomhumidity=x.get("roomhumidity")
bloodoxygenlevel=x.get("bloodoxygenlevel")
bodyweight=x.get("bodyweight")


med1=x.get("medicine1");
med2=x.get("medicine2");
med3=x.get("medicine3");
note=x.get("notes");



@app.route('/',methods = ['POST', 'GET'])
def pdf():

    return render_template('prescriptionpdf.html',pname=pname,med1=med1,med2=med2,med3=med3,note=note,dname=dname,
                           page=page,padhar=padhar,roomhumidity=roomhumidity,roomtemp=roomtemp,heartrate=heartrate,
                           bodytemp=bodytemp,bodyweight=bodyweight,opd=opd,bloodoxygenlevel=bloodoxygenlevel,date=date)


@app.route('/datapdf',methods = ['POST', 'GET'])
def dat():
    rf = request.form

    print("data")
    print(rf)
    return render_template('pdf.html',rf=rf)


if __name__ == "__main__":
    app.run(debug=True)
