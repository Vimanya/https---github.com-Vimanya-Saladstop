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
df = pd.read_csv (r'Path where the CSV file is saved\File Name.csv')
df.to_json (r'Path where the new JSON file will be stored\New File Name.json')
