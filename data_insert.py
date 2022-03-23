# importing pymongo
from pymongo import MongoClient

# establing connection
try:
    connect = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# connecting or switching to the database
db = connect.mydb

# creating or switching to demoCollection
collection = db.saladstop

import pandas as pd
df = pd.read_csv (r'saladstop.csv')
df.to_json (r'saladstop.json')
