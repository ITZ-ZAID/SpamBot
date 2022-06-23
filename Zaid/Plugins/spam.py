import asyncio

from pyrogram import filters, Client
from pyrogram.types import Message, User


@Client.on_message(filters.command('spam'))
async def spam(client: Client, message: Message):
    spam_text = ' '.join(message.command[2:])
    if not spam_text:
        await message.reply_text("Usage: \n\n/spam <count> message")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.1)
        return

    for _ in range(quantity):
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
