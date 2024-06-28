
import logging

import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from handlers.handler import router
from config import conf


load_dotenv()


async def on_startup(dp):
    pass


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


async def main() -> None:
    bot = Bot(token=conf.BOT_TOKEN)
    dp = Dispatcher(bot=bot)
    dp.include_routers(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())