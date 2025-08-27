
from pymongo import MongoClient
import os
# from dotenv import load_dotenv

# load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

db = client.notes
print(db.list_collection_names()) 
print(client.list_database_names())
user_collection = db["users"]
notes_collection = db["notes"]