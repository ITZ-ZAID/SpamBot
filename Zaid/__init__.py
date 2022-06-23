from pyrogram import Client, filters
from config import *

bot = Client("memory", plugins=dict(root="Zaid.Plugins"), bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
