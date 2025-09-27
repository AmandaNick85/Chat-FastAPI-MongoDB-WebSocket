<<<<<<< HEAD
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
load_dotenv(dotenv_path=ROOT / ".env")

MONGO_URL = os.getenv("MONGO_URL", "")
MONGO_DB = os.getenv("MONGO_DB", "chatdb")

if not MONGO_URL:
=======
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
load_dotenv(dotenv_path=ROOT / ".env")

MONGO_URL = os.getenv("MONGO_URL", "")
MONGO_DB = os.getenv("MONGO_DB", "chatdb")

if not MONGO_URL:
>>>>>>> 9eae65b6c3b70465fc97c7ec77022679ec47cce1
    raise ValueError("A variável de ambiente 'MONGO_URL' não está definida.")