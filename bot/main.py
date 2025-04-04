from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler  # This import was missing
from bot.config import API_ID, API_HASH, BOT_TOKEN, ADMINS
from handlers.message_handler import start, handle_video
from handlers.admin.stats import stats_command

app = Client(
    "FileSharingBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="handlers")
)

# Register handlers
app.add_handler(MessageHandler(start, filters.command("start")))  # Fixed extra parenthesis
app.add_handler(MessageHandler(handle_video, filters.video))
app.add_handler(MessageHandler(stats_command, filters.command("stats") & filters.user(ADMINS)))

if __name__ == "__main__":
    print("🤖 Bot starting...")
    app.run()
