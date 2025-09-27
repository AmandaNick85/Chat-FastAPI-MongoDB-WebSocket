from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from datetime import datetime, timezone
from app.config import MONGO_URL, MONGO_DB

_client: AsyncIOMotorClient | None = None

def get_db():
    global _client
    if _client is None:
        if not MONGO_URL:
            raise RuntimeError("Defina MONGO_URL no .env")
        try:
            _client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
            print("[INFO] Conexão com o MongoDB estabelecida com sucesso.")
        except Exception as e:
            raise ConnectionError(f"Erro ao conectar ao MongoDB: {e}")
    return _client[MONGO_DB]

def serialize(doc: dict) -> dict:
    if not doc:
        return {}

    d = dict(doc)
    if "_id" in d:
        d["_id"] = str(d["_id"])
    if "created_at" in d and isinstance(d["created_at"], datetime):
        if d["created_at"].tzinfo is None:
            d["created_at"] = d["created_at"].replace(tzinfo=timezone.utc)
        d["created_at"] = d["created_at"].isoformat()
    return d
