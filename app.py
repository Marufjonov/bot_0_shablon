import asyncio
import logging

from loader import bot, dp
# import middlewares, filters, handlers
from handlers import router as main_router

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)


async def on_startup():
    # Birlamchi komandalar (/start va /help)
    await set_default_commands(bot)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(bot)


async def main():
    logging.info("🚀 Bot polling boshlandi")
    dp.include_router(main_router)  # 🔥 MUHIM

    # 🔥 ENG MUHIM QATOR
    await on_startup()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("⛔ Bot to‘xtatildi (KeyboardInterrupt)")
