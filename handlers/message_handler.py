from pyrogram import filters
from bot.features.video_encoder import encode_video
from utils.logger import logger

async def handle_video(client, message):
    try:
        # Download the video
        video_path = await message.download()
        await message.reply("🚀 Processing your video...")
        
        # Encode video
        output_path = await encode_video(video_path, "720p")
        
        # Send encoded video back
        await message.reply_video(
            output_path,
            caption="✅ Your encoded video is ready!",
            progress=lambda current, total: logger.info(f"Uploaded {current * 100 / total:.1f}%")
            
    except Exception as e:
        logger.error(f"Video processing failed: {e}")
        await message.reply("❌ Failed to process video. Please try again.")
        
    finally:
        # Cleanup temporary files
        if 'video_path' in locals():
            os.remove(video_path)
        if 'output_path' in locals():
            os.remove(output_path)
