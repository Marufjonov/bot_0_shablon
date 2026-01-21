from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message
from typing import Optional

router = Router()

@router.message(CommandStart())
@router.message(CommandStart(deep_link=True))
async def bot_start(
    message: Message,
    command: Optional[CommandObject] = None,
):
    args = command.args if command else None

    text = f"Salom, {message.from_user.full_name}!\n"
    if args:
        text += f"Sizni {args} tavsiya qildi"
    else:
        text += "Oddiy /start bosildi"

    await message.answer(text)
