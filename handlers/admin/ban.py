from pyrogram import filters

async def ban_user(client, message):
    target = message.reply_to_message.from_user.id
    await client.ban_chat_member(message.chat.id, target)
    await message.reply("User banned! 🚫")
