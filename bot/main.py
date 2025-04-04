from pyrogram import Client, filters, idle  # <-- 'idle' ইম্পোর্ট যোগ করুন
from pyrogram.handlers import MessageHandler
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from bot.config import API_ID, API_HASH, BOT_TOKEN, ADMINS
from handlers.message_handler import start, handle_video
from handlers.admin.stats import stats_command

# হেলথ চেক সার্ভার সেটআপ
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')

def run_health_server():
    server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
    print("🩺 হেলথ চেক সার্ভার চালু হয়েছে (পোর্ট 8080)")
    server.serve_forever()

# Pyrogram ক্লায়েন্ট ইনিশিয়ালাইজ
app = Client(
    "FileSharingBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

# হ্যান্ডলার রেজিস্টার করুন
app.add_handler(MessageHandler(start, filters.command("start")))
app.add_handler(MessageHandler(handle_video, filters.video))
app.add_handler(MessageHandler(stats_command, filters.command("stats") & filters.user(ADMINS)))

if __name__ == "__main__":
    # হেলথ সার্ভার স্টার্ট করুন (মূল থ্রেডে)
    health_thread = threading.Thread(target=run_health_server, daemon=True)
    health_thread.start()
    
    print("🤖 বট চালু হচ্ছে...")
    app.start()  # Pyrogram ম্যানুয়ালি স্টার্ট করুন
    idle()  # বটকে একটিভ রাখুন
    app.stop()
