from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
STRING_SESSION1 = getenv("STRING_SESSION1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = getenv("OWNER_ID", "1603412565")
BOT_VER = "1.1.5@main"
BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_URL = getenv("MONGO_URL", "")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/55d4f8d54263f20fbcb31.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "")
PM_LOGGER = getenv("PM_LOGGER")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/sip-userbot/Shicyproject")
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HANDLER = getenv("CMD_HANDLER", "")
DB_URL = getenv("DATABASE_URL", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")
STRING_SESSION16 = getenv("STRING_SESSION16", "")
STRING_SESSION17 = getenv("STRING_SESSION17", "")
STRING_SESSION18 = getenv("STRING_SESSION18", "")
STRING_SESSION19 = getenv("STRING_SESSION19", "")
STRING_SESSION20 = getenv("STRING_SESSION20", "")
