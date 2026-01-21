from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def bot_help(message: Message):
    text = (
        "📌 Buyruqlar:",
        "/start - Botni ishga tushirish",
        "/help - Yordam",
        "/settings - Sozlamalar",
    )

    await message.answer("\n".join(text))


@router.message(Command("settings"))
async def bot_help(message: Message):
    text = ( "Sozlamalar")

    await message.answer(text)