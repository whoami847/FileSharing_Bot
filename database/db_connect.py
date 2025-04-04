from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)
db = client["FileSharingBot"]
