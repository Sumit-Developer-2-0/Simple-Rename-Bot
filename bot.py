import os
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, DOWNLOAD_LOCATION


class Bot(Client):
    def __init__(self):
        if not os.path.isdir(DOWNLOAD_LOCATION):
            os.makedirs(DOWNLOAD_LOCATION)
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} | @{me.username} STARTED...⚡️")

    async def stop(self, *args):
        await super().stop()
        print("Bot Restarting........")
     app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()


if __name__ == "__main__":
    bot = Bot()
    bot.run()
