import asyncio
from aiogram import Bot, Dispatcher
from handlers import register_all_handlers

BOT_TOKEN = ""


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    register_all_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
