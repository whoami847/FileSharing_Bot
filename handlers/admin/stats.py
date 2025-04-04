from pyrogram import filters
from bot.config import ADMINS
from utils.logger import logger

async def stats_command(client, message):
    if message.from_user.id not in ADMINS:
        return
    stats_text = "📊 **Bot Stats:**\nUsers: 100\nFiles: 50"
    await message.reply_text(stats_text)
