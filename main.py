#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 2195251, #get it from https://my.telegram.org/auth
    api_hash="d9bc5c3d73b1c50433effaf504ed12af", #get it from https://my.telegram.org/auth
    bot_token="6010702251:AAFVuSZNq1B0oOBiIhZoIzYsEZacx_JA_T8", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
    
