import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load .env variables (MONGODB_URI, DB_NAME, COLLECTION_NAME)
load_dotenv()

# Read environment variables
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "biomarker_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "extracted_articles")

# Initialize MongoDB client and connect to DB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def insert_article(data: dict):
    """
    Insert a dictionary representing one article into MongoDB.
    Returns the MongoDB document ID.
    """
    result = collection.insert_one(data)
    return result.inserted_id

def get_all_articles():
    """
    Fetch all documents in the collection as a list of dictionaries
    """
    return list(collection.find())

