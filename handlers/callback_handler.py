from pyrogram.types import CallbackQuery

async def handle_quality_selection(client, callback_query: CallbackQuery):
    quality = callback_query.data
    await callback_query.answer(f"Selected {quality}p")
    await client.send_message(
        callback_query.message.chat.id,
        f"Encoding in {quality}p..."
    )
