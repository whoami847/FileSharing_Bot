from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from bot.config import API_ID, API_HASH, BOT_TOKEN, ADMINS
from handlers.message_handler import start, handle_video  # ✅ start ইম্পোর্ট করা হয়েছে
from handlers.admin.stats import stats_command

app = Client(
    "FileSharingBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

# হ্যান্ডলার রেজিস্টার করুন
app.add_handler(MessageHandler(start, filters.command("start")))  # ✅ start এখন ডিফাইন করা আছে
app.add_handler(MessageHandler(handle_video, filters.video))
app.add_handler(MessageHandler(stats_command, filters.command("stats") & filters.user(ADMINS)))

if __name__ == "__main__":
    print("🤖 বট চালু হচ্ছে...")
    app.run()
