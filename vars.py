from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = int(environ.get("API_ID", "1460778"))
API_HASH = environ.get("API_HASH", "b61dce498a5cb53a72f610b8e7f3c13a")
BOT_TOKEN = environ.get("BOT_TOKEN", "6207520435:AAG1Ox1s9nctvw7_geR1fwotsh_-R52jNH8")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001809210997"))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1365371238 1129673243 5394954571').split()]
TARGET_DB = int(environ.get("TARGET_DB"," -1001760325016"))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/Joelkb/File-Forward-Bot")
