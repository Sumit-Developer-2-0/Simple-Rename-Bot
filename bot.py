import os
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, DOWNLOAD_LOCATION
from aiohttp import web  # Make sure to import web if you're using it

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
        print("Bot is stopping...")

async def web_server():
    # Define your web server logic here
    app = web.Application()
    # Add routes and handlers to your app
    return app

if __name__ == "__main__":
    bot = Bot()

    # Start the bot and the web server
    async def main():
        await bot.start()
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        PORT = 8080  # Define your port here
        await web.TCPSite(app, bind_address, PORT).start()
        print(f"Web server started on {bind_address}:{PORT}")
        await idle()  # Keep the bot running

    import asyncio
    asyncio.run(main())
