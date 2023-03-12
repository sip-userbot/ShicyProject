import logging
import time
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOTLOG_CHATID, DB_URL, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10, STRING_SESSION11, STRING_SESSION12, STRING_SESSION13, STRING_SESSION14, STRING_SESSION15, STRING_SESSION16, STRING_SESSION17, STRING_SESSION18, STRING_SESSION19, STRING_SESSION20
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiohttp import ClientSession
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
from pytgcalls import GroupCallFactory

CMD_HELP = {}

StartTime = time.time()

START_TIME = datetime.now()

TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}


SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)

if BOTLOG_CHATID:
    BOTLOG_CHATID = BOTLOG_CHATID
else:
    BOTLOG_CHATID = "me"

LOOP = asyncio.get_event_loop()

aiosession = ClientSession()

scheduler = AsyncIOScheduler()

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

if API_ID:
   API_ID = API_ID
else:
   print("WARNING: INITIALIZING APP ID ")
   API_ID = "6435225"

if API_HASH:
   API_HASH = API_HASH
else:
   print("WARNING: INITIALIZING APP HASH ")   
   API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
   print("WARNING: BOT TOKEN NOT FOUND PLZ ADD ")

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Shicy/modules/bot"),
    in_memory=True,
)

if STRING_SESSION1:
   print("Client1: Found.. Starting..")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="Shicy/modules"))
   clients.append(client1)

if STRING_SESSION2:
   print("Client2: Found.. Starting.. ")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="Shicy/modules"))
   clients.append(client2)

if STRING_SESSION3:
   print("Client3: Found.. Starting.. ")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="Shicy/modules"))
   clients.append(client3)

if STRING_SESSION4:
   print("Client4: Found.. Starting.. ")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="Shicy/modules"))
   clients.append(client4)

if STRING_SESSION5:
   print("Client5: Found.. Starting.. ")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="Shicy/modules"))
   clients.append(client5)

if STRING_SESSION6:
   print("Client6: Found.. Starting.. ")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="Shicy/modules"))
   clients.append(client6)

if STRING_SESSION7:
   print("Client7: Found.. Starting.. ")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="Shicy/modules"))
   clients.append(client7)

if STRING_SESSION8:
   print("Client8: Found.. Starting.. ")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="Shicy/modules"))
   clients.append(client8)

if STRING_SESSION9:
   print("Client9: Found.. Starting.. ")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="Shicy/modules"))
   clients.append(client9)

if STRING_SESSION10:
   print("Client10: Found.. Starting.. ")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="Shicy/modules")) 
   clients.append(client10)

if STRING_SESSION11:
   print("Client1: Found.. Starting..")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="Shicy/modules"))
   clients.append(client1)

if STRING_SESSION12:
   print("Client2: Found.. Starting.. ")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="Shicy/modules"))
   clients.append(client2)

if STRING_SESSION13:
   print("Client3: Found.. Starting.. ")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="Shicy/modules"))
   clients.append(client3)

if STRING_SESSION14:
   print("Client4: Found.. Starting.. ")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="Shicy/modules"))
   clients.append(client4)

if STRING_SESSION15:
   print("Client5: Found.. Starting.. ")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="Shicy/modules"))
   clients.append(client5)

if STRING_SESSION16:
   print("Client6: Found.. Starting.. ")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="Shicy/modules"))
   clients.append(client6)

if STRING_SESSION17:
   print("Client7: Found.. Starting.. ")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="Shicy/modules"))
   clients.append(client7)

if STRING_SESSION18:
   print("Client8: Found.. Starting.. ")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="Shicy/modules"))
   clients.append(client8)

if STRING_SESSION19:
   print("Client9: Found.. Starting.. ")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="Shicy/modules"))
   clients.append(client9)

if STRING_SESSION20:
   print("Client10: Found.. Starting.. ")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="Shicy/modules")) 
   clients.append(client10)

client = [client for client in[STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10, STRING_SESSION11, STRING_SESSION12, STRING_SESSION13, STRING_SESSION14, STRING_SESSION15, STRING_SESSION16, STRING_SESSION17, STRING_SESSION18, STRING_SESSION19, STRING_SESSION20]if client]

for client in clients:
    if not hasattr(client, "group_call"):
        setattr(client, "group_call", GroupCallFactory(client).get_group_call())
