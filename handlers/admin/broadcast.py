from pyrogram import filters
from database.models import User

async def broadcast_message(client, message):
    users = await User.collection.find().to_list(None)
    for user in users:
        await client.send_message(user["id"], message.text)
