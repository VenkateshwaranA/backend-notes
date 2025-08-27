from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from models.notes import Notes, User, Userlogin
from config.database import notes_collection, user_collection
from schema.schemas import list_serial
from bson import ObjectId
from controllers.controller import create_user, authenticate_user, create_notes,get_items, update_Note,delete_note
from auth.jwt import create_access_token

router = APIRouter()


@router.get("/")
async def get_notes():
    notes = list_serial(notes_collection.find())
    return notes


@router.post("/register")
async def register(user: User):
    print(f"userrr, {user}")
    if not create_user(user.email, user.password, user.userName):
        raise HTTPException(status_code=400, detail="User already exists")
    return {"msg": "User registered"}


@router.post("/login")
async def login(user: Userlogin):
    print(f"userrr login --->, {user}")
    db_user = authenticate_user(user.email, user.password)
    print(f"authecicateeee --->, {db_user}")
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(db_user)
    return {"access_token": token}


@router.post("/notes")
async def add_item(item: Notes):
    item_id = create_notes(item.user_id, item.note_title, item.note_content)
    return {"item_id": item_id}


@router.get("/notes/{user_id}")
async def list_items(user_id: str):
    items = get_items(user_id)
    return items

@router.put("/note/{note_id}")
async def update(note_id: str, item: Notes, ):
    count = update_Note(note_id, item.dict())
    if count == 0:
        raise HTTPException(status_code=404, detail="Item not found or not updated")
    return {"msg": "Updated"}

@router.delete("/note/{note_id}")
async def delete(note_id: str):
    count = delete_note(note_id)
    if count == 0:
        raise HTTPException(status_code=404, detail="Item not found or not deleted")
    return {"msg": "Deleted"}
