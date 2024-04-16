from pyrogram import filters
from pyrogram.types import Message
import nekos
from StringGen import Anony
from StringGen.utils import add_served_user, keyboard
import requests
import random
import os
import re
from os import getenv
import time


LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002041372224"))


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_photo(
        photo=nekos.img("neko"),
        caption=f"ʜᴇʏ {message.from_user.mention},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nAɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.",
        reply_markup=keyboard,
     #   disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
    await Anony.send_message(
                LOG_GROUP_ID,
                f"{message.from_user.mention} has just started Bot.\n\n**USER ID:** {message.from_user.id}\n**USER NAME:** {message.from_user.username}",
        )
