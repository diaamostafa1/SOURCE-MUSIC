from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/e4fe42e42e1f40c59e8a8.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/e4fe42e42e1f40c59e8a8.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Sp_M0m2nt")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/M0M2NT")

MOMENT_USERS = list(map(int, getenv("MOMENT_USERS", "1593971384").split()))


FAILED = "https://graph.org/file/e4fe42e42e1f40c59e8a8.jpg"
