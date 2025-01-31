import time
import os
from pyrogram import Client, filters, enums
from config import DOWNLOAD_LOCATION, CAPTION, ADMIN
from main.utils import progress_message, humanbytes


@Client.on_message(filters.private & filters.command("rename") & filters.user(ADMIN))
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    if not reply or len(msg.command) < 2:
        return await msg.reply_text(
            "Please reply to a file with the new filename. Example: `/rename newfile.mp4`"
        )

    media = reply.document or reply.audio or reply.video
    if not media:
        return await msg.reply_text(
            "Please reply to a file with the new filename. Example: `/rename newfile.mp4`"
        )

    og_media = getattr(reply, reply.media.value)
    new_name = msg.text.split(" ", 1)[1].strip()

    if not new_name:
        return await msg.reply_text("Please provide a valid file name")
        
    sts = await msg.reply_text("Trying to download...")
    c_time = time.time()
    try:
        downloaded = await reply.download(
            file_name=new_name, progress=progress_message, progress_args=("Download Started...", sts, c_time)
        )
    except Exception as e:
        return await sts.edit(f"Download failed: {e}")

    filesize = humanbytes(og_media.file_size)

    if CAPTION:
        try:
            cap = CAPTION.format(file_name=new_name, file_size=filesize)
        except Exception as e:
            return await sts.edit(
                f"Error formatting caption: {e}."
            )
    else:
        cap = f"{new_name}\n\n💽 size : {filesize}"

    # Thumbnail handling logic
    file_thumb = None
    if not os.listdir(DOWNLOAD_LOCATION):  # More efficient check for an empty dir
        try:
            if og_media.thumbs:
                file_thumb = await bot.download_media(og_media.thumbs[0].file_id)
                og_thumbnail = file_thumb
            else:
                og_thumbnail = None  # No thumbnail available
        except Exception as e:
                print(f"Error downloading original thumb: {e}")
                og_thumbnail = None 

    else:
        try:
            og_thumbnail = f"{DOWNLOAD_LOCATION}/thumbnail.jpg"  # Presumed path to thumbnail
            if not os.path.exists(og_thumbnail):
                og_thumbnail = None
                print(f"Warning: {og_thumbnail} doesn't exist")
        except Exception as e:
            print(f"Error thumbnail path: {e}")
            og_thumbnail = None
    
    await sts.edit("Trying to upload...")
    c_time = time.time()

    try:
        await bot.send_document(
            msg.chat.id,
            document=downloaded,
            thumb=og_thumbnail,
            caption=cap,
            progress=progress_message,
            progress_args=("Upload Started...", sts, c_time),
        )
    except Exception as e:
        return await sts.edit(f"Upload failed: {e}")
    finally:
            
        try:
            if file_thumb:
                os.remove(file_thumb)
            os.remove(downloaded)  
        except Exception as e:
            print(f"Error during cleanup: {e}")

    await sts.delete()