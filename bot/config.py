import os
from dotenv import load_dotenv

load_dotenv()

# Essential Telegram Configuration
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "FileSharingBot")

# Admin Configuration
ADMINS = list(map(int, os.getenv("ADMINS", "").split()))
OWNER_ID = int(os.getenv("OWNER_ID", 0))

# Optional Configuration
CHANNEL_ID = int(os.getenv("CHANNEL_ID", -100))
PROTECT_CONTENT = os.getenv("PROTECT_CONTENT", "False") == "True"
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 1200))

# Validate essential configuration
if not all([API_ID, API_HASH, BOT_TOKEN, DATABASE_URL]):
    raise ValueError("Missing required environment variables!")
