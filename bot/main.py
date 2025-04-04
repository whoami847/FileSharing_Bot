from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from bot.config import API_ID, API_HASH, BOT_TOKEN, ADMINS
from handlers import message_handler, callback_handler
from handlers.admin import stats, ban, broadcast

app = Client("FileSharingBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register handlers properly
app.add_handler(MessageHandler(message_handler.start, filters.command("start")))
app.add_handler(MessageHandler(message_handler.handle_video, filters.video))
app.add_handler(MessageHandler(stats.stats_command, filters.command("stats") & filters.user(ADMINS)))

if __name__ == "__main__":
    app.run()
