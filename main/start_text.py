import html
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import ADMIN

def back_button():
    return InlineKeyboardButton("⬅️ Back", callback_data="start")

def close_button():
    return InlineKeyboardButton("🚫 Close", callback_data="del")


@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, msg):
    txt = "This is a personal use bot 🙏. Do you want your own bot? 👇 Click the source code to deploy"
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🤖 SOURCE CODE", url="https://github.com/Sumit-Developer-2-0/Simple-Rename-Bot")
            ],
            [
                InlineKeyboardButton("🖥️ How To Deploy", url="https://youtu.be/oc847WvOUaI")
            ],
        ]
    )
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview=True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):
    txt = f"Hai {msg.from_user.mention}, I am a simple rename bot for personal use. This bot is made by <b><a href=https://github.com/Sumit-Developer-2-0>Sumit-Developer-2-0</a></b>"
    button = [
        [
            InlineKeyboardButton("🤖 Bot Updates", url="https://t.me/sumit_bots_updates")
        ],
        [
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
            InlineKeyboardButton("📡 About", callback_data="about")
        ]
    ]
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "Just send a file and `/rename <new name>` with the replied file.\n\n"
    txt += "Send a photo to set a thumbnail automatically.\n"
    txt += "/view to see your thumbnail.\n"
    txt += "/del to delete your thumbnail."
    button = [
        [
            close_button(),
            back_button()
        ]
    ]
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me = await bot.get_me()
    Master = f"<a href=https://t.me/Mo_Tech_YT>MoTech</a> & <a href=https://t.me/sumitbotupdates>MhdRzn</a>"
    Source = "<a href=https://github.com/Sumit-Developer-2-0/Simple-Rename-Bot>Click Here</a>"
    txt = f"<b>Bot Name: {html.escape(me.first_name)}\nDeveloper: <a href=https://github.com/MrMKN>MrMKN</a>\nBot Updates: <a href=https://t.me/sumit_bots_updates>sumit BᴏᴛZ™</a>\nMy Master's: {Master}\nSource Code: {Source}</b>"
    button = [
        [
            close_button(),
            back_button()
        ]
    ]
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return