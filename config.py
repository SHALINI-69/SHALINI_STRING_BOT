from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Haamerijaan84:8548965250@cluster9.soj0lsu.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 1356469075))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/music_world_sh")
