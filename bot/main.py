from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from bot.config import API_ID, API_HASH, BOT_TOKEN, ADMINS

app = Client(
    "FileSharingBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,  # ✅ সেশন মেমরিতে স্টোর হবে
    workers=2,  # ✅ কানেকশন স্ট্যাবিলিটি জন্য
    sleep_threshold=30  # ✅ টাইমআউট এড়াতে
)

# হ্যান্ডলার যোগ করুন
app.add_handler(MessageHandler(start, filters.command("start")))
app.add_handler(MessageHandler(handle_video, filters.video))

if __name__ == "__main__":
    print("🤖 বট স্টার্ট হয়েছে!")
    app.run()
