import os
from pyrogram import Client, filters
from config import ADMIN, DOWNLOAD_LOCATION


@Client.on_message(filters.private & filters.photo & filters.user(ADMIN))
async def set_tumb(bot, msg):
    thumb_path = f"{DOWNLOAD_LOCATION}/thumbnail.jpg"
    try:
        await bot.download_media(msg.photo, file_name=thumb_path)
        await msg.reply(
            "Your permanent thumbnail is saved ✅.\n"
            "If you change your server or recreate the server app, you'll need to reset your thumbnail.⚠️"
        )
    except Exception as e:
        print(f"Error saving thumbnail: {e}")
        await msg.reply("Error saving thumbnail.")


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))
async def view_tumb(bot, msg):
    thumb_path = f"{DOWNLOAD_LOCATION}/thumbnail.jpg"
    if os.path.exists(thumb_path):
        try:
            await msg.reply_photo(photo=thumb_path, caption="This is your current thumbnail.")
        except Exception as e:
            print(f"Error sending thumbnail: {e}")
            await msg.reply_text("Error sending the thumbnail.")

    else:
        await msg.reply_text("You don't have any thumbnail set.")


@Client.on_message(filters.private & filters.command(["del", "del_thumb"]) & filters.user(ADMIN))
async def del_tumb(bot, msg):
    thumb_path = f"{DOWNLOAD_LOCATION}/thumbnail.jpg"
    if os.path.exists(thumb_path):
        try:
            os.remove(thumb_path)
            await msg.reply_text("Your thumbnail was removed. 🚫")
        except Exception as e:
            print(f"Error deleting thumbnail: {e}")
            await msg.reply_text("Error deleting the thumbnail.")
    else:
        await msg.reply_text("You don't have any thumbnail set.")