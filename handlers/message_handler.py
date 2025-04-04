from pyrogram import filters
from bot.features.video_encoder import encode_video

async def handle_video(client, message):
    video = await message.download()
    await message.reply("Processing your video...")
    output_path = await encode_video(video, "720p")
    await message.reply_video(output_path)
