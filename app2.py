import cluster as cluster
import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request,redirect, url_for
import pandas as pd
import os
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import json
import base64

now = datetime.now() # current date and time
today=now.strftime("%m-%d-%Y")
print(today)
app = Flask(__name__)

cluster = MongoClient("mongodb+srv://arpit:567arpit@cluster0.ot8xk.mongodb.net/rx?retryWrites=true&w=majority")
db = cluster["rx"]








collection = db["patient"]


#03-14-2021
#mhwe1234
# @app.route('/<adhar>/<date>',methods = ['POST', 'GET'])
# def pdf(adhar,date):
#     print(adhar+" "+date)
#     x = collection.find_one({"date": date, "padhar": adhar})
#     print(x)
#
#     date = x["date"]
#     dname = x["dname"]
#     pname = x["pname"]
#     padhar = x["padhar"]
#     page = x["page"]
#     roomtemp = x["roomtemp"]
#     heartrate = x["heartrate"]
#     bodytemp = x["bodytemp"]
#     opd = x["opd"]
#     roomhumidity = x["roomhumidity"]
#     bloodoxygenlevel = x["bloodoxygenlevel"]
#     bodyweight = x["bodyweight"]
#
#     med1 = x["medicine1"]
#     med2 = x["medicine2"]
#     med3 = x["medicine3"]
#     note = x["notes"]
#
#     return render_template('pdf.html',pname=pname,med1=med1,med2=med2,med3=med3,note=note,dname=dname,
#                            page=page,padhar=padhar,roomhumidity=roomhumidity,roomtemp=roomtemp,heartrate=heartrate,
#                            bodytemp=bodytemp,bodyweight=bodyweight,opd=opd,bloodoxygenlevel=bloodoxygenlevel,date=date)
#
roomTemp = 0
roomHumid = 0
heartRate = 0
bloodOxy = 0
bodyTemp = 0















@app.route('/register', methods=['POST', 'GET'])
def register():
	monitor = int(request.args.get('monitor', 0))
	roomTemp = 0
	roomHumid = 0
	heartRate = 0
	bloodOxy = 0
	bodyTemp = 0
	pName = ''
	age = 0
	aadhar = 0
	opd = 0
	weight = 0

	if monitor == 0:

		return render_template('register.html', roomTemp=roomTemp, roomHumid=roomHumid, heartRate=heartRate,
		                       bloodOxy=bloodOxy, bodyTemp=bodyTemp)

	elif monitor == 1:

		url = "http://localhost:8000/index.html"

		source = requests.get(url)

		soup = BeautifulSoup(source.text, 'lxml')

		roomTemp = int(soup.findAll("div", {"class": "roomTemp"})[0].contents[0])
		roomHumid = int(soup.findAll("div", {"class": "roomHumid"})[0].contents[0])
		heartRate = int(soup.findAll("div", {"class": "heartRate"})[0].contents[0])
		bloodOxy = int(soup.findAll("div", {"class": "bloodOxy"})[0].contents[0])
		bodyTemp = int(soup.findAll("div", {"class": "bodyTemp"})[0].contents[0])

		return render_template('register.html', roomTemp=roomTemp, roomHumid=roomHumid, heartRate=heartRate,
							   bloodOxy=bloodOxy, bodyTemp=bodyTemp, pName=pName, age=age, aadhar=aadhar, opd=opd,
							   weight=weight)


	elif monitor == 2:

		data = request.args.get('data')
		data = base64.b64decode(data)
		data = data.decode("utf-8")
		data = json.loads(data)
		print(data)

		pName = data['pName']
		age = int(data['age'])
		aadhar = (data['aadhar'])
		opd = int(data['opd'])
		weight = int(data['weight'])

		post1 = {

			"pname": pName,
			"padhar": aadhar,
			"page": age,
			"roomtemp": roomTemp,
			"heartrate": heartRate,
			"bodytemp": bodyTemp,
			"opd": opd,
			"roomhumidity": roomHumid,
			"bloodoxygenlevel": bloodOxy,
			"bodyweight": weight

		}

		collection.insert_one(post1)
		print("inserted successfully")

		return render_template('register.html', roomTemp=roomTemp, roomHumid=roomHumid, heartRate=heartRate,
							   bloodOxy=bloodOxy, bodyTemp=bodyTemp, pName=pName, age=age, aadhar=aadhar, opd=opd,
							   weight=weight)

	elif monitor == 3:

		data = request.args.get('data')
		data = base64.b64decode(data)
		data = data.decode("utf-8")
		data = json.loads(data)

		pName = data['pName']
		age = int(data['age'])
		aadhar = (data['aadhar'])
		opd = int(data['opd'])
		weight = int(data['weight'])

		'''
        Try to put your code here
        '''

		#
		# url = "http://localhost:8000/index.html"
		#
		# source = requests.get(url)
		#
		# soup = BeautifulSoup(source.text, 'lxml')
		#
		# roomTemp = int(soup.findAll("div", {"class": "roomTemp"})[0].contents[0])
		# roomHumid = int(soup.findAll("div", {"class": "roomHumid"})[0].contents[0])
		# heartRate = int(soup.findAll("div", {"class": "heartRate"})[0].contents[0])
		# bloodOxy = int(soup.findAll("div", {"class": "bloodOxy"})[0].contents[0])
		# bodyTemp = int(soup.findAll("div", {"class": "bodyTemp"})[0].contents[0])

		print(pName, age, aadhar, bloodOxy, bodyTemp)
		return redirect(url_for('regpdf',adhar=aadhar))



@app.route('/registerpdf/<adhar>',methods = ['POST', 'GET'])

def regpdf(adhar):

    print(adhar+" ")

    x = collection.find_one({ "padhar": adhar})
    print(x)


    pname = x["pname"]
    padhar = x["padhar"]
    page = x["page"]
    roomtemp = x["roomtemp"]
    heartrate = x["heartrate"]
    bodytemp = x["bodytemp"]
    opd = x["opd"]
    roomhumidity = x["roomhumidity"]
    bloodoxygenlevel = x["bloodoxygenlevel"]
    bodyweight = x["bodyweight"]

    return render_template('registerpdf.html',pname=pname,
                           page=page,padhar=padhar,roomhumidity=roomhumidity,roomtemp=roomtemp,heartrate=heartrate,
                           bodytemp=bodytemp,bodyweight=bodyweight,opd=opd,bloodoxygenlevel=bloodoxygenlevel)











if __name__ == "__main__":
    app.run(debug=True)
