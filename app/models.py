<<<<<<< HEAD
from pydantic import BaseModel, Field
from datetime import datetime

class MessageIn(BaseModel):
    username: str = Field(..., max_length=50)
    content: str = Field(..., min_length=1, max_length=1000)

class MessageOut(BaseModel):
    _id: str
    room: str
    username: str
    content: str
    created_at: datetime
=======
from pydantic import BaseModel, Field
from datetime import datetime

class MessageIn(BaseModel):
    username: str = Field(..., max_length=50)
    content: str = Field(..., min_length=1, max_length=1000)

class MessageOut(BaseModel):
    _id: str
    room: str
    username: str
    content: str
    created_at: datetime
>>>>>>> 9eae65b6c3b70465fc97c7ec77022679ec47cce1
