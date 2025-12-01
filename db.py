import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # load .env file

MONGODB_URI = os.getenv("MONGODB_URI") or "mongodb://localhost:27017/"
client = MongoClient(MONGODB_URI)
db = client["university_db"]  # database name
