import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 7217645
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"

BOT_TOKEN = "2100096282:AAGisj7MdXcXXRD-DmJ2ix8E-FmbrUNVtEM"

MONGO_DB_URI = "mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
LOG_GROUP_ID = -1001564289796
MUSIC_BOT_NAME = "Fantastic"

OWNER_ID = [1793699293]

HEROKU_API_KEY = None
HEROKU_APP_NAME = None

UPSTREAM_REPO = "https://github.com/Roninopp/sexi"
UPSTREAM_BRANCH = "master"
GIT_TOKEN = None

SUPPORT_CHANNEL = "https://t.me/Fantastic_support"
SUPPORT_GROUP = "Fantastic_support"


DURATION_LIMIT_MIN = 180
SONG_DOWNLOAD_DURATION = 180

AUTO_LEAVING_ASSISTANT = "False"
AUTO_LEAVE_ASSISTANT_TIME = int(
    "5400"
)

AUTO_DOWNLOADS_CLEAR = "True"

PRIVATE_BOT_MODE = None

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int("5")
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int("3")

SPOTIFY_CLIENT_ID = None
SPOTIFY_CLIENT_SECRET = None

VIDEO_STREAM_LIMIT = int("5")
SERVER_PLAYLIST_LIMIT = int("50")
PLAYLIST_FETCH_LIMIT = int("50")

CLEANMODE_DELETE_MINS = int("12")

TG_AUDIO_FILESIZE_LIMIT = int("104857600")
TG_VIDEO_FILESIZE_LIMIT = int("1073741824")
# https://www.gbmb.org/mb-to-bytes

STRING1 = "BQAQ8mzivK_5gCuVFuCoTSsVryMtuWzw80gJR0IUa_es4frLORBcJipeK1qiHmUWcShsBb9MKyN-TiyJFw9zXFWl1XqAtIXXHLhYxGkFZ-W3VFQWOT7-F1J4arXV2ly_y6FDv_uK_bWXBB0GU2AFf6fj3wT0AJ0Ny2KFPYawYHHIXFobiNj4tNlHEqWIarTCiLEFcJgmbbhobpZPJVUmwq7dmwXnjG0xouIqMEUy_jV1ZyM7OFbBaSyc2bc9BuZvee-B2OW5bGNxY8fWD5v6cWUuAcN_z5BSr2wcM_h-X99uM1rno93Z8e0OjR0AK3eLldEp44LuOPn58whTKzZUAAAAAUK509kA"
STRING2 = None
STRING3 = None
STRING4 = None
STRING5 = None

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

PING_IMG_URL = (

    "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

STATS_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/56d1760224589ee370186.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg"
