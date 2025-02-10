import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "26489431"))
API_HASH = os.getenv("API_HASH", "9a2fce85339bb79254a55368a61ab92f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7544054473:AAG9aWU4amrjzz-34x9nGKQX-kG3-EVEQxo")
ADMIN = int(os.getenv("ADMIN", "7912527708"))
CAPTION = os.getenv("CAPTION", "{file_name}\n\n💽 Size = {file_size}\n\n📯Join My Channel : @mkn_bots_updates")

# for thumbnail ( back end is MrMKN brain 😉)
DOWNLOAD_LOCATION = "./DOWNLOADS"

if API_ID == 0 or not API_HASH or not BOT_TOKEN or ADMIN == 0:
    print("ERROR: Environment variables not set properly. Please check your .env file.")
    exit()
