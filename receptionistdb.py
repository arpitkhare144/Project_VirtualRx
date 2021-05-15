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



app = Flask(__name__)

cluster = MongoClient("mongodb+srv://arpit:567arpit@cluster0.ot8xk.mongodb.net/rx?retryWrites=true&w=majority")
db = cluster["rx"]
collection=db["receptionist"]
print("receptionist created")

post1={
    "rusername":"merry", "rpassword":"1234merry"
}
post2={
    "rusername":"chris", "rpassword":"1234chris"
}
post3={
    "rusername":"rohit", "rpassword":"1234rohit"
}
post4={
    "rusername":"harry", "rpassword":"1234harry"
}
post5={
    "rusername":"jarvis", "rpassword":"hellotonysir"
}

collection.insert_one(post1)
collection.insert_one(post2)
collection.insert_one(post3)
collection.insert_one(post4)
collection.insert_one(post5)
print("post inserted successfully")