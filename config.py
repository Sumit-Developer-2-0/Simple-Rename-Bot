import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", "0"))
CAPTION = os.getenv("CAPTION", "")

# for thumbnail ( back end is MrMKN brain 😉)
DOWNLOAD_LOCATION = "./DOWNLOADS"

if API_ID == 0 or not API_HASH or not BOT_TOKEN or ADMIN == 0:
    print("ERROR: Environment variables not set properly. Please check your .env file.")
    exit()