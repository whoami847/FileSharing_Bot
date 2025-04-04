from pyrogram import Client, filters
from bot.config import API_ID, API_HASH, BOT_TOKEN
from handlers import message_handler, callback_handler
from handlers.admin import stats, ban, broadcast

app = Client("FileSharingBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

app.add_handler(filters.command("start")(message_handler.start))
app.add_handler(filters.video)(message_handler.handle_video))
app.add_handler(filters.command("stats") & filters.user(ADMINS))(stats.stats_command))

app.run()
