# COPYRIGHT (C) 2021 BY LEGENDX22
"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
"""
# MADE BY LEGENDX22 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
from userbot.utils import admin_cmd as legendx 
api_id = os.environ.get("APP_ID", None)
api_hash = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
import os
from userbot import botnickname, ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", api_id, api_hash).start(bot_token=token)
BOT = str(botnickname) if botnickname else "LEGEND BOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOY"
PHOTO = os.environ.get("ALIVE_PHOTTO", "https://telegra.ph/file/00353e01b4e05d26568fc.jpg")
LEGENDX = "[LEGEND X](https://t.me/LEGENDX22)"
REPO = "[LEGEND BOT](https://github.com/LEGENDXOP/LEGEND-BOT)"
PRO = bot.uid
MASTER = f"[{NAME}](tg://user?id={PRO})"
GROUP = "[SUPPORT GROUP](https://t.me/LEGEND_USERBOT_SUPPORT)"
if __name__=="__main__":
  xbot.start()
  xbot.run_until_disconnected()
