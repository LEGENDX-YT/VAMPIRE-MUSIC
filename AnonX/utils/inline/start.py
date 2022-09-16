from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="★彡[ADD ME TO YOUƦ GƦOUᴩ]彡★",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="★彡[ʜᴇʟᴘ]彡★",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="★彡[ꜱᴇᴛᴛɪɴɢꜱ]彡★", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="★彡[ᴏᴡɴᴇʀ]彡★", user_id=OWNER),
            InlineKeyboardButton(
                text="★彡[ꜱᴜᴘᴘᴏʀᴛ]彡★", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="★彡[ADD ME TO YOUƦ GƦOUᴩ]彡★",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="★彡[ʜᴇʟᴘ]彡★", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴍᴀɪɴᴛᴀɪɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="★彡[ꜱᴜᴘᴘᴏʀᴛ]彡★", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="꧁𓊈𒆜🆂ᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜʏ𒆜𓊉꧂", url=f"https://t.me/ULTRONBOY_XD"
                )
        ],
     ]
    return buttons
