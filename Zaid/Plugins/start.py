from pyrogram import Client, filters

@Client.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello, This Is Spam Bot Based On PyroGram!")
