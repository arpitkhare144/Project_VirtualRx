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
import math
import ssl
from collections import OrderedDict
now = datetime.now() # current date and time
today=now.strftime("%m-%d-%Y")
print(today)
app = Flask(__name__)

cluster = MongoClient("mongodb+srv://arpitkhare:567arpit@cluster0.ot8xk.mongodb.net/rx?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = cluster["rx"]

logindoctor=False






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








usernamer =""





app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    count=collection.count()
    print("count:"+str(count))
    return render_template('homepage.html',count=count)


@app.route('/loginselect', methods=['POST', 'GET'])
def loginselect():

    return render_template('selectlogin.html')

@app.route('/loginreceptionist', methods=['POST', 'GET'])
def login():
    return render_template('sample.html')

@app.route('/logindoctor', methods=['POST', 'GET'])
def logindoctor():
    return render_template('login.html')

@app.route('/listview/<aadhar>', methods=['POST', 'GET'])
def listview(aadhar):
    dlist= {"date":"","padhar":""}
    collection=db["prescription"]
    x=collection.find({"padhar":aadhar})

    datelist = []

    for doc in x:
        print(doc.get("date"))
        pdate=doc.get("date")
        datelist.append(pdate)
        dlist["date"]+=" "+pdate
        datelist.append(pdate)
        dlist["padhar"]+=" "+(doc.get("padhar"))
    print(dlist)

    return render_template('listview.html', datelist=datelist,aadhar=aadhar)

@app.route('/registervalidation', methods=['POST', 'GET'])
def registervalidation():


    if request.method == 'POST':
        result = request.form
        global usernamer
        usernamer = str(result.get('username')) + ""
        print(usernamer)

        password = str(result.get('password')) + ""
        print(password)
        collection = db["receptionist"]
        # print("doctorimages created")
        rep = collection.find_one({"rusername": usernamer})
        print(rep)
        if (rep != None):
            print("**********valid username************")
            print(rep)
            pswd = rep["rpassword"]
            print(pswd)
            currpswd = password
            if (pswd == currpswd):
                print("**********valid password************")
                # global logindoctor
                # logindoctor = True
                # return render_template('adhariddoctor.html', doctor=username)
                return redirect(url_for('register'))
    return render_template('sample.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
            # if request.method == 'POST':
            #     result = request.form
            #     username = str(result.get('username')) + ""
            #     print(username)
            #
            #     password = str(result.get('password')) + ""
            #     print(password)
            #     collection = db["receptionist"]
            #     # print("doctorimages created")
            #     rep = collection.find_one({"rusername": username})
            #     print(rep)
            #     if (rep != None):
            #         print("**********valid username************")
            #         print(rep)
            #         pswd = rep["rpassword"]
            #         print(pswd)
            #         currpswd = password
            #         if (pswd == currpswd):
            #             print("**********valid password************")
            #             # global logindoctor
            #             # logindoctor = True
            #             # return render_template('adhariddoctor.html', doctor=username)


                        monitor = int(request.args.get('monitor', 0))
                        global roomTemp, roomHumid, heartRate, bloodOxy, bodyTemp
                        pName = ''
                        age = 0
                        aadhar = 0
                        opd = 0
                        weight = 0
                        print("monitor")
                        print(monitor)
                        if monitor == 0:

                            return render_template('register.html', roomTemp=roomTemp, roomHumid=roomHumid, heartRate=heartRate,
                                                   bloodOxy=bloodOxy, bodyTemp=bodyTemp,pName=pName,age=age,aadhar=aadhar,opd=opd,weight=weight,username=usernamer)

                        elif monitor == 1:

                            # data = request.args.get('data')
                            # data = base64.b64decode(data)
                            # data = data.decode("utf-8")
                            # data = json.loads(data)
                            # print(data)
                            #
                            # pName = data['pName']
                            # age = int(data['age'])
                            # aadhar = int(data['aadhar'])
                            # opd = int(data['opd'])
                            # weight = int(data['weight'])

                            url = "http://localhost:8000/index.html"

                            source = requests.get(url)

                            soup = BeautifulSoup(source.text, 'lxml')

                            roomTemp = int(soup.findAll("div", {"class": "roomTemp"})[0].contents[0])
                            roomHumid = int(soup.findAll("div", {"class": "roomHumid"})[0].contents[0])
                            heartRate = int(soup.findAll("div", {"class": "heartRate"})[0].contents[0])
                            bloodOxy = int(soup.findAll("div", {"class": "bloodOxy"})[0].contents[0])
                            bodyTemp = int(soup.findAll("div", {"class": "bodyTemp"})[0].contents[0])

                            return render_template('register.html', roomTemp=roomTemp, roomHumid=roomHumid, heartRate=heartRate,
                                                   bloodOxy=bloodOxy, bodyTemp=bodyTemp,pName=pName,age=age,aadhar=aadhar,opd=opd,weight=weight,username=usernamer)

                        elif monitor == 2:

                            data = request.args.get('data')
                            data = base64.b64decode(data)
                            data = data.decode("utf-8")
                            data = json.loads(data)

                            pName = data['pName']
                            age = int(data['age'])
                            aadhar = (data['aadhar'])
                            opd = int(data['opd'])
                            weight = int(data['weight'])

                            k = len(str(aadhar))
                            if(k == 12):
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
                                #
                                print(pName)
                                # print(bodyTemp)

                                return render_template('register.html', roomTemp=roomTemp, roomHumid=roomHumid, heartRate=heartRate,
                                                    bloodOxy=bloodOxy, bodyTemp=bodyTemp,pName=pName,age=age,aadhar=aadhar,opd=opd,weight=weight,username=usernamer)
                            
                            return render_template('register.html', roomTemp=roomTemp, roomHumid=roomHumid, heartRate=heartRate,
                                                    bloodOxy=bloodOxy, bodyTemp=bodyTemp,pName=pName,age=age,aadhar=aadhar,opd=opd,weight=weight,username=usernamer)

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


                            print(pName,age,aadhar,bloodOxy,bodyTemp)
                            if(len(str(aadhar)) == 12):
                                return redirect(url_for('regpdf',adhar=aadhar))
                            return render_template('register.html', roomTemp=roomTemp, roomHumid=roomHumid, heartRate=heartRate,
                                                    bloodOxy=bloodOxy, bodyTemp=bodyTemp,pName=pName,age=age,aadhar=aadhar,opd=opd,weight=weight,username=usernamer)
                            # return render_template('sample.html')
            # return render_template('sample.html')

@app.route('/registerpdf/<adhar>',methods = ['POST', 'GET'])

def regpdf(adhar):

    print(adhar+" ")
    collection.find().sort("_id",-1)
    x = collection.find_one({ "padhar": adhar})
    print(x)
    resultset = collection.find().sort("_id", -1)
    for r in resultset:
        if (r["padhar"] == adhar):
            print('match')
            print(r)
            x = r
            break

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





@app.route('/pdf/<adhar>/<date>',methods = ['POST', 'GET'])
def pdf(adhar,date):
    collection = db["prescription"]

    print(adhar+" "+date)
    # collection.sort({"_id": -1})
    x = collection.find_one({"padhar":adhar,"date":date})
    print("data")
    print(x)

    date = x["date"]
    dname = x["dname"]
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

    noofmed=len(x)-14;
    i=0;
    print("noofmedicine "+str(noofmed))
    medarr=list()
    while(i<noofmed):
        medarr.append(x["medicine "+str(i)].replace("\r",""))
        i+=1
    print(medarr)

    #med1 = x["medicine 0"].replace("\r","")
    #med2 = x["medicine 1"].replace("\r","")
    #med3 = x["medicine3"]
    note = x["notes"]
    print("data")
    #print(pname+" "+med1+" "+med2+" "+note+" "+dname+" "+date)
    return render_template('prescriptionpdf2.html',pname=pname,note=note,dname=dname,
                           page=page,padhar=padhar,roomhumidity=roomhumidity,roomtemp=roomtemp,heartrate=heartrate,
                           bodytemp=bodytemp,bodyweight=bodyweight,opd=opd,bloodoxygenlevel=bloodoxygenlevel,date=date,medarr=medarr,i=noofmed)

@app.route('/pdfpatient/<adhar>/<date>',methods = ['POST', 'GET'])
def pdfpatient(adhar,date):
    collection = db["prescription"]
    # collection.sort({"_id": -1})
    print(adhar+" "+date)
    x = collection.find_one({"padhar":adhar,"date":date})
    print("data")
    print(x)

    date = x["date"]
    dname = x["dname"]
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

    noofmed=len(x)-14;
    i=0;
    print("noofmedicine "+str(noofmed))
    medarr=list()
    while(i<noofmed):
        medarr.append(x["medicine "+str(i)].replace("\r",""))
        i+=1
    print(medarr)

    #med1 = x["medicine 0"].replace("\r","")
    #med2 = x["medicine 1"].replace("\r","")
    #med3 = x["medicine3"]
    note = x["notes"]
    print("data")
    #print(pname+" "+med1+" "+med2+" "+note+" "+dname+" "+date)
    return render_template('pdfadharpatientside.html',pname=pname,note=note,dname=dname,
                           page=page,padhar=padhar,roomhumidity=roomhumidity,roomtemp=roomtemp,heartrate=heartrate,
                           bodytemp=bodytemp,bodyweight=bodyweight,opd=opd,bloodoxygenlevel=bloodoxygenlevel,date=date,medarr=medarr,i=noofmed)





@app.route('/patientlistview/<aadhar>', methods=['POST', 'GET'])
def listviewpatient(aadhar):
    dlist= {"date":"","padhar":""}
    collection=db["prescription"]
    # collection.sort({"_id": -1})
    x=collection.find({"padhar":aadhar})

    datelist = []

    for doc in x:
        print(doc.get("date"))
        pdate=doc.get("date")
        datelist.append(pdate)
        dlist["date"]+=" "+pdate
        datelist.append(pdate)
        dlist["padhar"]+=" "+(doc.get("padhar"))
    print(dlist)


    return render_template('precribtionlist.html', datelist=datelist,aadhar=aadhar)



@app.route('/patientlistviewp/<aadhar>', methods=['POST', 'GET'])
def listviewpatientp(aadhar):
    dlist= {"date":"","padhar":""}
    collection=db["prescription"]
    # collection.sort({"_id": -1})
    x=collection.find({"padhar":aadhar})
    print(x)
    datelist = []

    for doc in x:
        print(doc)
        print(doc.get("date"))
        pdate=doc.get("date")
        datelist.append(pdate)
        dlist["date"]+=" "+pdate
        datelist.append(pdate)
        dlist["padhar"]+=" "+(doc.get("padhar"))
    print(dlist)
    dict1 = OrderedDict(sorted(dlist.items()))
    print(dict1)


    return render_template('prescriptionlistpatient.html', datelist=datelist,aadhar=aadhar)



@app.route('/patientlistviewnavbar/<aadhar>', methods=['POST', 'GET'])
def listviewpatientnavbar(aadhar):
    return render_template('prescriptionlistpatientnavbar.html',aadhar=aadhar)


@app.route('/doctorpatientlistview/<aadhar>/<doctor>', methods=['POST', 'GET'])
def listviewpatientdoctor(aadhar,doctor):
    dlist= {"date":"","padhar":""}
    collection=db["prescription"]
    # collection.sort({"_id": -1})
    x=collection.find({"padhar":aadhar})

    datelist = []

    for doc in x:
        print(doc.get("date"))
        pdate=doc.get("date")
        datelist.append(pdate)
        dlist["date"]+=" "+pdate
        datelist.append(pdate)
        dlist["padhar"]+=" "+(doc.get("padhar"))
    print(dlist)

    return render_template('prescriptionlistdoctor.html', datelist=datelist,aadhar=aadhar,doctor=doctor)


@app.route('/doctorpatientlistviewnavbar/<aadhar>/<doctor>', methods=['POST', 'GET'])
def listviewpatientdoctornavbar(aadhar,doctor):
    print("value of login")
    print(logindoctor)
    print(doctor)
    precent="%40"
    if precent in doctor:
        demo1="arpit@gmail.com"
        print(demo1)
        demo1.replace("@","#")
        print(demo1)
        doctor=doctor.replace("%40","@")
        print("inside if")
    print(doctor)
    if(logindoctor==True):

        dlist= {"date":"","padhar":""}
        collection=db["prescription"]
        x=collection.find({"padhar":aadhar})

        datelist = []

        for doc in x:
            print(doc.get("date"))
            pdate=doc.get("date")
            datelist.append(pdate)
            dlist["date"]+=" "+pdate
            datelist.append(pdate)
            dlist["padhar"]+=" "+(doc.get("padhar"))
        print(dlist)
        collection = db["doctorimages"]
        print("doctorimages created")
        print(collection)
        pimg = collection.find_one({"dusername":doctor})
        print(pimg)
        pimgimg = pimg["dprofile"]
        design = pimg["designation"]
        degree = pimg["degree"]
        dname=pimg["dname"]
        return render_template('prescriptionlistdoctornavbar.html', datelist=datelist,aadhar=aadhar,doctor=dname,pimgimg=pimgimg,design=design,degree=degree,did=doctor)
    return  render_template('logindoctor.html')


@app.route('/docpatientadhar/<doctor>', methods=['POST', 'GET'])
def adharpatient(doctor):
        return render_template('adhariddoctor.html',doctor=doctor)


@app.route('/docpatientadharvalidationnavbar/<doctor>', methods=['POST', 'GET'])
def adharpatientvalidationnavbar(doctor):

    return render_template('adhariddoctornavbar.html',doctor=doctor)

@app.route('/docpatientadharvalidation', methods=['POST', 'GET'])
def adharpatientvalidation():


    if request.method == 'POST':
        result = request.form
        username = str(result.get('username'))+""
        print(username)

        password = str(result.get('password'))+""
        print(password)
        collection = db["doctorimages"]
        print("doctorimages created")
        pimg = collection.find_one({"dusername": username})
        print(pimg)
        if (pimg != None):
            print("**********valid username************")
            print(pimg)
            pswd = pimg["dpassword"]
            print(pswd)
            currpswd = password
            if (pswd == currpswd):
                print("**********valid password************")
                global logindoctor
                logindoctor=True
                pimgimg=pimg["dprofile"]
                design=pimg["designation"]
                degree=pimg["degree"]
                return render_template('adhariddoctor.html', doctor=pimg["dname"],did=username,pimgimg=pimgimg,design=design,degree=degree)




    return render_template('logindoctor.html')

@app.route('/doctorlogout', methods=['POST', 'GET'])
def doctorlogout():
    global logindoctor
    logindoctor = False
    return render_template('logindoctor.html');

@app.route('/logindoctorvalidation', methods=['POST', 'GET'])
def logindoctorvalidation():
    return render_template('logindoctor.html')


@app.route('/threebutton/<aadhar>/<doctor>', methods=['POST', 'GET'])
def threebutton(aadhar,doctor):
    return render_template('threebutton.html',aadhar=aadhar,doctor=doctor)

@app.route('/twobutton/<aadhar>', methods=['POST', 'GET'])
def twobutton(aadhar):
    return render_template('twobutton.html',aadhar=aadhar)

@app.route('/doctorlogindash/<doctor>', methods=['POST', 'GET'])
def doctorlogindash(doctor):
    collection = db["doctorimages"]
    print("doctorimages created")
    print("logindash")
    print("doctor:"+str(doctor))
    pimg = collection.find_one({"dusername": doctor})
    print("longindash pimg")
    print(pimg)
    print(pimg["dprofile"])
    design = pimg["designation"]
    degree = pimg["degree"]
    dname = pimg["dname"]
    return render_template('dash.html',doctor=dname,pimg=pimg["dprofile"],design=design,degree=degree)


@app.route('/patientadhar', methods=['POST', 'GET'])
def adharpatient2():
    return render_template('adharid.html')


@app.route('/patientprofile/<adhar>', methods=['POST', 'GET'])
def profilepatient(adhar):

    collection = db["patient"]

    # collection.find({}).sort("_id", -1)
    print(adhar + " ")

    x = collection.find_one({"padhar": adhar})
    print(x)
    resultset = collection.find().sort("_id", -1)
    for r in resultset:
        if(r["padhar"]==adhar):
            print('match')
            print(r)
            x=r
            break
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
    return render_template('patientprofile.html',aadhar=adhar,pname=pname,page=page,padhar=padhar,roomhumidity=roomhumidity,roomtemp=roomtemp,heartrate=heartrate,
                           bodytemp=bodytemp,bodyweight=bodyweight,opd=opd,bloodoxygenlevel=bloodoxygenlevel)



@app.route('/drop/<adhar>/<dname>',methods = ['POST', 'GET'])
def drop(adhar,dname):


    df = pd.read_csv('data1.csv')
    df = pd.read_csv('data1.csv')
    final = list(df["Name"])
    inal = list(df["Name"])
    dict1 = df.to_dict()
    # print(dict1)
    # print(final)
    print("drop")
    return render_template('drop.html', username=dname,medicine=final,adhar=adhar,date=today,dname=dname)
    # df = pd.read_csv('data1.csv')
    # final = list(df["Name"])
    # print(final)






@app.route('/<adhar>/<dname>',methods = ['POST', 'GET'])
def middle(adhar,dname):


    if request.method == 'POST':
        result = request.form
        username = result.get('data')
        print(username)
        username=username.replace("Delete","")
        s=username.split("\n")
        print(s)
        medicine=list()
        print("\n")
        print("----------------------------------------------------------------------------------------------------------------")
        i=0
        while i < (len(s)-1):
            medicine.append("Medicine Name: "+s[i].replace("\xa0\xa0","").replace("\r","")+"----- Dosage: "+s[i+1].replace("\xa0\xa0","").replace("\xa0\xa0",""))
            i+=2
        for i in range(len(medicine)):
            print(medicine[i])
        notes= result.get('notes')
        print(notes)
        collection = db["patient"]
        print(adhar + " ")

        x = collection.find_one({"padhar": adhar})
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

        collection = db["prescription"]
        post={

            "date":today,
            "dname":dname,
            "pname":pname,
            "padhar":padhar,
            "page":page,
            "roomtemp":roomtemp,
            "heartrate":heartrate,
            "bodytemp":bodytemp,
            "opd":opd,
            "roomhumidity":roomhumidity,
            "bloodoxygenlevel":bloodoxygenlevel,
            "bodyweight":bodyweight,

            "notes":notes

        }
        for i in range(len(medicine)):
            post["medicine "+str(i)]=medicine[i]
        collection.insert_one(post)

        return redirect(url_for('pdf',adhar=padhar,date=today))

@app.route('/framedash',methods = ['POST', 'GET'])
def framedash():
    return render_template("framedash.html")





if __name__ == "__main__":
    app.run(debug=True)
