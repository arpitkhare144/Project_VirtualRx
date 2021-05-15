import cluster as cluster
import pymongo
from pymongo import MongoClient
from datetime import datetime

now = datetime.now() # current date and time
today=now.strftime("%m-%d-%Y")

print(today)
cluster = MongoClient("mongodb+srv://arpit:567arpit@cluster0.ot8xk.mongodb.net/rx?retryWrites=true&w=majority")
db = cluster["rx"]
collection=db["doctor"]

#post1={"did":"D1","dusername":"doctorstrak","dpassword":"doctor12345","dname":"jhon","dcontact":"0987765432",
#      "ddept":"OPD","deducation":"MS","dexperience":"5 years","dspec":"kidney"}

#collection.insert_one(post1)

x=collection.find_one({"did":"D3"})
print(x)

collection=db["patient"]
# post1={
#
# "pname":"arpit khare",
# "padhar":"mhwe1234",
# "page":45,
# "roomtemp":"10",
# "heartrate":"55",
# "bodytemp":"35",
# "opd":"opd1",
# "roomhumidity":"20",
# "bloodoxygenlevel":"100",
# "bodyweight":"45"
# }
# post2={
#
# "pname":"sumeet gedam",
# "padhar":"mhwe1236",
# "page":23,
# "roomtemp":"20",
# "heartrate":"45",
# "bodytemp":"35",
# "opd":"opd2",
# "roomhumidity":"20",
# "bloodoxygenlevel":"89",
# "bodyweight":"45"
# }
# post3={
#
# "pname":"sarang mishra",
# "padhar":"uhwe1236",
# "page":23,
# "roomtemp":"20",
# "heartrate":"35",
# "bodytemp":"25",
# "opd":"opd2",
# "roomhumidity":"20",
# "bloodoxygenlevel":"89",
# "bodyweight":"60"
# }
# post4={
#
# "pname":"aryan gupta",
# "padhar":"mhwe1237",
# "page":23,
# "roomtemp":"20",
# "heartrate":"45",
# "bodytemp":"35",
# "opd":"opd2",
# "roomhumidity":"20",
# "bloodoxygenlevel":"89",
# "bodyweight":"45"
# }

# collection.insert_one(post1)
# collection.insert_one(post2)
# collection.insert_one(post3)
# collection.insert_one(post4)
x=collection.find_one({"pname":"arpit khare"})
print(x.get("pname"))

#
collection=db["prescription"]
#
post1={
"date":today,
"dname":"jhon",
"pname":"arpit khare",
"padhar":"mhwe1234",
"page":45,
"roomtemp":"10",
"heartrate":"55",
"bodytemp":"35",
"opd":"opd1",
"roomhumidity":"20",
"bloodoxygenlevel":"100",
"bodyweight":"45",
"medicine1":"crocin  before breafast|after lunch|before dinner",
"medicine2":"syrup  before breafast|after lunch|before dinner",
"medicine3":"hajmola  before breafast|after lunch|before dinner",
"notes":"drink more water"
}
# post2={
# "date":today,
# "dname":"jhon",
# "pname":"sumeet gedam",
# "padhar":"mhwe1236",
# "page":23,
# "roomtemp":"20",
# "heartrate":"45",
# "bodytemp":"35",
# "opd":"opd2",
# "roomhumidity":"20",
# "bloodoxygenlevel":"89",
# "bodyweight":"45",
# "medicine1":"crocin  before breafast|after lunch|before dinner",
# "medicine2":"syrup  before breafast|after lunch|before dinner",
# "medicine3":"hajmola  before breafast|after lunch|before dinner",
# "notes":"drink more water"
# }
# post3={
# "date":today,
# "dname":"jhon",
# "pname":"sarang mishra",
# "padhar":"uhwe1236",
# "page":23,
# "roomtemp":"20",
# "heartrate":"35",
# "bodytemp":"25",
# "opd":"opd2",
# "roomhumidity":"20",
# "bloodoxygenlevel":"89",
# "bodyweight":"60",
# "medicine1":"crocin  before breafast|after lunch|before dinner",
# "medicine2":"syrup  before breafast|after lunch|before dinner",
# "medicine3":"hajmola  before breafast|after lunch|before dinner",
# "notes":"drink more water"
# }
# post4={
# "date":today,
# "dname":"jhon",
# "pname":"aryan gupta",
# "padhar":"mhwe1237",
# "page":23,
# "roomtemp":"20",
# "heartrate":"45",
# "bodytemp":"35",
# "opd":"opd2",
# "roomhumidity":"20",
# "bloodoxygenlevel":"89",
# "bodyweight":"45",
# "medicine1":"crocin  before breafast|after lunch|before dinner",
# "medicine2":"syrup  before breafast|after lunch|before dinner",
# "medicine3":"hajmola  before breafast|after lunch|before dinner",
# "notes":"drink more water"
# }
#
collection.insert_one(post1)
# collection.insert_one(post2)
# collection.insert_one(post3)
# collection.insert_one(post4)

x=collection.find_one({"date":today})
print(x)