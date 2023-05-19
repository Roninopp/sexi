import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 7217645
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"

BOT_TOKEN = "2100096282:AAHFyyJsiWXgUuR5kaahD_kKwH6h2CoNJE8"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://FantasticRobot:FantasticRobot@cluster0.8ka4syj.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = -1001564289796
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Fantastic")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1793699293").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Roninopp/sexi")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Fantastic_support")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Fantastic_support")


DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQCXZtz_GWZGhAmPl7k_zs3ZvoLY3FSHig7LxZv2_F1LPot6Nd0xWou6s-zVTd5tXFhehylYOKyHdvkUFtI20U3Xf1ZJp5ITo2uHmcXuq_CSUV5P0i32rNEv9Wm0d1udH6qZt5bdAo6OEVR0cqYsnX7cA6-oVOoTLikIJOn8PXi6_xMcnGls-RAdkT98s4_TXF15iJZ9OK_MGUMbFgpYlHNeiWOqmQJ-4MMHKRtKwj5VSizZlkFVoh3qG4YNsny_r7m4c-VhpMmfOvVzM7tsK9kiP7aA3uSrWe7J64iRiqVpPo8UMN5DLCAoJWrw49GQk2NDgHalD3S8hGmuGAj64Q7xAAAAAUK509kA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

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


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/124fbf1cb443e09c2062c.jpg",
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
