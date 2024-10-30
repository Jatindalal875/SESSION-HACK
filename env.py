import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "12834603")
API_HASH = os.getenv("API_HASH", "84a5daf7ac334a70b3fbd180616a76c6")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6671551975:AAGgRjNnA7Sb11l2d493EA7s03c8lVW5Ef4")
SUDOERS = list(map(int, os.getenv("SUDOERS", "5615344987").split()))
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Rone:rone@cluster0.sln9j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", "-1001815554788")
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/ELENAMUSICSUPPORT")
DISABLED = os.getenv("DISABLED", "").split()

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
