import math
import time

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

PROGRESS_BAR = "\n\n📁 : {b} | {c}\n🚀 : {a}%\n⚡ : {d}/s\n⏱️ : {f}"
REFRESH_INTERVAL = 5  # Update the progress message every 5 seconds


async def progress_message(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff) % REFRESH_INTERVAL == 0 or current == total:
        percentage = (current * 100) / total
        speed = current / diff if diff else 0  # Avoid division by zero
        elapsed_time = int(diff * 1000)
        remaining_time = int(((total - current) / speed) * 1000) if speed else 0
        estimated_total_time = elapsed_time + remaining_time

        elapsed_time = time_formatter(elapsed_time)
        estimated_total_time = time_formatter(estimated_total_time)

        progress = "\n{0}{1}".format(
            "".join(["⬢" for _ in range(math.floor(percentage / 5))]),
            "".join(["⬡" for _ in range(20 - math.floor(percentage / 5))]),
        )

        tmp = progress + PROGRESS_BAR.format(
            a=round(percentage, 2),
            b=humanbytes(current),
            c=humanbytes(total),
            d=humanbytes(speed),
            f=estimated_total_time if estimated_total_time else "0 s",
        )
        try:
            chance = [[InlineKeyboardButton("🚫 Cancel", callback_data="del")]]
            await message.edit(text=f"{ud_type}\n{tmp}", reply_markup=InlineKeyboardMarkup(chance))
        except:
            pass


def humanbytes(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return f"{size:.2f} {units[i]}"


def time_formatter(milliseconds: int) -> str:
    if milliseconds == 0:
        return "0s"
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    time_parts = []
    if days:
        time_parts.append(f"{days}d")
    if hours:
        time_parts.append(f"{hours}h")
    if minutes:
        time_parts.append(f"{minutes}m")
    if seconds:
      time_parts.append(f"{seconds}s")
    if not days and not hours and not minutes:
        time_parts.append(f"{milliseconds}ms")
    return ", ".join(time_parts)