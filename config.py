# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29905645"))
API_HASH = getenv("API_HASH", "e5a701f6e0b5fb659cb57a230b9a3feb")
BOT_TOKEN = getenv("BOT_TOKEN", "7311671831:AAG_kDJkKT57WNyM3klVf8L3zzzqk7nwDMI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8102112566").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Technicalankit:Technicalankit@cluster0.dzl9fbr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002756256056")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002756256056"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "100"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "gplinks.com")
AD_API = getenv("AD_API", "29905645")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
