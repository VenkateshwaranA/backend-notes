from config.database import user_collection, notes_collection
from auth.jwt import hash_password, verify_password
from bson import ObjectId
from datetime import datetime


def create_user(email, password, userName):
    if user_collection.find_one({"email": email}):
        return None
    hashed_pw = hash_password(password)
    user_doc = {
        "email": email,
        "userName": userName,
        "password": hashed_pw,
        "created_on": datetime.utcnow(),
        "last_update": datetime.utcnow()
    }

    user_collection.insert_one(user_doc)
    return True


def authenticate_user(email, password):
    user = user_collection.find_one({"email": email})
    print(F"ssssssssssssss, {user}")
    if user and verify_password(password, user["password"]):
        return user
    return None


def create_notes(user_id, title, content=""):
    print(f"{user_id}, {title},SDsdsdsdsd")
    item = {"note_title": title, "note_content": content, "user_id": user_id, "created_on": datetime.utcnow(),
            "last_update": datetime.utcnow()}
    result = notes_collection.insert_one(item)
    return str(result.inserted_id)


def get_items(userId: str):
    items = list(notes_collection.find({"user_id": userId}))
    for item in items:
        item["_id"] = str(item["_id"])  
    return items

def update_Note(item_id, data):
    result = notes_collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": data}
    )
    return result.modified_count


def delete_note(item_id):
    result = notes_collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count
