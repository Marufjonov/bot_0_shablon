from aiogram.types import BotCommand

async def set_default_commands(bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam"),
    ])
