
from pymongo import MongoClient
import pandas as pd

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["predictive_analysis"]

# Collection
customers = db["customers"]

data = list(customers.find())

df = pd.DataFrame(data)


print(df.head())