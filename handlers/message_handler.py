from pyrogram import filters
import os
from bot.features.video_encoder import encode_video
from utils.logger import logger
from datetime import datetime

# Track bot start time for uptime calculation
START_TIME = datetime.now()

async def start(client, message):
    try:
        await message.reply_text(
            "🎥 Welcome to File Sharing Bot!\n"
            "Send me a video to encode it to 720p/480p!\n\n"
            "📌 Available commands:\n"
            "/start - Show this message\n"
            "/stats - Show bot statistics (Admin only)"
        )
    except Exception as e:
        logger.error(f"Start command failed: {e}")

async def handle_video(client, message):
    try:
        video_path = await message.download()
        logger.info(f"Downloaded video to: {video_path}")
        await message.reply("🚀 Processing your video...")
        
        output_path = await encode_video(video_path, "720p")
        logger.info(f"Encoded video saved to: {output_path}")
        
        await message.reply_video(
            video=output_path,
            caption="✅ Your encoded video is ready!",
            progress=lambda current, total: logger.debug(f"Upload progress: {current}/{total} bytes")
        )
            
    except Exception as e:
        logger.error(f"Video processing failed: {e}")
        await message.reply("❌ Failed to process video. Please try again.")
        
    finally:
        for path in [video_path, output_path]:
            try:
                if path and os.path.exists(path):
                    os.remove(path)
                    logger.debug(f"Cleaned up: {path}")
            except Exception as e:
                logger.warning(f"Cleanup failed for {path}: {e}")

def get_uptime():
    return str(datetime.now() - START_TIME).split('.')[0]
