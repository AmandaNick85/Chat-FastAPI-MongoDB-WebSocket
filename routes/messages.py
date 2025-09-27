from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from bson import ObjectId
from app.database import get_db, serialize
from app.models import MessageIn, MessageOut
from datetime import datetime, timezone

router = APIRouter()

@router.get("/rooms/{room}/messages")
async def get_messages(room: str, limit: int = Query(20, ge=1, le=100), before_id: Optional[str] = None):
    query = {"room": room}
    if before_id:
        try:
            query["_id"] = {"$lt": ObjectId(before_id)}
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid before_id")
    cursor = get_db()["messages"].find(query).sort("_id", -1).limit(limit)
    docs = [serialize(d) async for d in cursor]
    docs.reverse()
    next_cursor = docs[0]["_id"] if docs else None
    return {"items": docs, "next_cursor": next_cursor}

@router.post("/rooms/{room}/messages", status_code=201)
async def post_message(room: str, message: MessageIn):
    doc = {
        "room": room,
        "username": message.username,
        "content": message.content,
        "created_at": datetime.now(timezone.utc)
    }
    res = await get_db()["messages"].insert_one(doc)
    doc["_id"] = res.inserted_id
    return serialize(doc)
