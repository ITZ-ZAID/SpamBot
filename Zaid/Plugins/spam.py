import asyncio

from pyrogram import filters, Client
from pyrogram.types import Message, User


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id



@Client.on_message(filters.command("spam", "!"))
async def spam(bot: Client, message: Message):
    # Get current chat and spam to there.
    # if in group and replied to user, then spam replying to user.
    await message.delete()

    times = message.command[1]
    to_spam = " ".join(message.command[2:])

    if message.chat.type in ["supergroup", "group"]:
        for _ in range(int(times)):
            await bot.send_message(
                message.chat.id, to_spam, reply_to_message_id=ReplyCheck(message)
            )
            await asyncio.sleep(0.20)

    if message.chat.type == "private":
        for _ in range(int(times)):
            await bot.send_message(message.chat.id, to_spam)
            await asyncio.sleep(0.20)


