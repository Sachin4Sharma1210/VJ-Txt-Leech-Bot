# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import time
import asyncio
from datetime import timedelta
from pyrogram.errors import FloodWait

class Timer:
    def __init__(self, time_between=5):
        self.time_between = time_between
        self.last_time = 0

    async def can_send(self):
        now = time.time()
        if now - self.last_time >= self.time_between:
            self.last_time = now
            return True
        return False


def hrb(value, digits=2, delim="", postfix="", binary=True):
    """Human-readable file size"""
    if value is None:
        return None
    units = ["B", "KiB", "MiB", "GiB", "TiB"] if binary else ["B", "KB", "MB", "GB", "TB"]
    step = 1024 if binary else 1000
    for unit in units:
        if value < step:
            return f"{value:.{digits}f}{delim}{unit}{postfix}"
        value /= step
    return f"{value:.{digits}f}{delim}{units[-1]}{postfix}"


def hrt(seconds, precision=0):
    """Human-readable time delta"""
    pieces = []
    value = timedelta(seconds=int(seconds))

    if value.days:
        pieces.append(f"{value.days}d")

    seconds = value.seconds
    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}h")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}m")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}s")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])


timer = Timer()


async def progress_bar(current, total, reply, start):
    if await timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return

        perc = f"{current * 100 / total:.1f}%"
        elapsed_time = round(diff)
        speed = max(current / elapsed_time, 0.0001)
        remaining_bytes = total - current
        eta_seconds = remaining_bytes / speed
        eta = hrt(eta_seconds, precision=1)

        sp = str(hrb(speed)) + "/s"
        tot = hrb(total)
        cur = hrb(current)

        # Dynamic progress bar
        bar_length = 15
        completed_length = int(current * bar_length / total)
        remaining_length = bar_length - completed_length
        progress_bar_str = "🔵" * completed_length + "⚪" * remaining_length

        message_text = (
            f"<b>\n"
            f"╭──⌯════🆄︎ᴘʟᴏᴀᴅɪɴɢ⬆️⬆️═════⌯──╮\n"
            f"├⚡ {progress_bar_str} | {perc}\n"
            f"├🚀 Speed » {sp}\n"
            f"├📟 Processed » {cur}\n"
            f"├🧲 Size - ETA » {tot} - {eta}\n"
            f"├⏱️ Elapsed » {hrt(elapsed_time, precision=1)}\n"
            f"├🤖 𝔹ʏ » 👑 𝕊𝔸ℂℍ𝕀ℕ 𝕊ℍ𝔸ℝ𝕄𝔸 👑\n"
            f"╰─═══ ✪👑 @sachin4sharma1210 👑✪ ═══─╯\n"
            f"</b>"
        )

        try:
            await reply.edit(message_text)
        except FloodWait as e:
            await asyncio.sleep(e.x)
