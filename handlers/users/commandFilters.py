from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()



@router.message(Command('til'))
async def changeLanguage(message: Message):
    text = ( "Til o'zgardi")

    await message.answer(text)