from pyrogram import filters
import os
from bot.features.video_encoder import encode_video
from utils.logger import logger

async def start(client, message):
    await message.reply_text(
        "🎥 Welcome to File Sharing Bot!\n"
        "Send me a video to encode it to 720p/480p!"
    )

async def handle_video(client, message):
    try:
        video_path = await message.download()
        await message.reply("🚀 Processing your video...")
        
        output_path = await encode_video(video_path, "720p")
        
        await message.reply_video(
            output_path,
            caption="✅ Your encoded video is ready!",
            progress=lambda current, total: logger.info(f"Uploaded {current * 100 / total:.1f}%")
        )
            
    except Exception as e:
        logger.error(f"Video processing failed: {e}")
        await message.reply("❌ Failed to process video. Please try again.")
        
    finally:
        if 'video_path' in locals() and os.path.exists(video_path):
            os.remove(video_path)
        if 'output_path' in locals() and os.path.exists(output_path):
            os.remove(output_path)
