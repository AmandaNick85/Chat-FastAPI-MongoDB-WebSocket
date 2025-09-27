from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import messages
from app.ws_manager import WSManager
from app.database import get_db, serialize
from app.models import MessageIn
from datetime import datetime, timezone

app = FastAPI(title="Chat FastAPI + MongoDB")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(messages.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

manager = WSManager()

@app.get("/", include_in_schema=False)
async def index():
    return FileResponse("app/static/index.html")

@app.websocket("/ws/{room}")
async def ws_room(ws: WebSocket, room: str):
    await manager.connect(room, ws)
    try:
        cursor = get_db()["messages"].find({"room": room}).sort("_id", -1).limit(20)
        items = [serialize(d) async for d in cursor]
        items.reverse()
        await ws.send_json({"type": "history", "items": items})

        while True:
            payload = await ws.receive_json()
            try:
                message = MessageIn(**payload)
            except Exception:
                continue

            doc = {
                "room": room,
                "username": message.username,
                "content": message.content,
                "created_at": datetime.now(timezone.utc)
            }
            result = await get_db()["messages"].insert_one(doc)
            doc["_id"] = result.inserted_id
            await manager.broadcast(room, {"type": "message", "item": serialize(doc)})

    except WebSocketDisconnect:
        manager.disconnect(room, ws)

