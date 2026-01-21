from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter

router = Router()

# Echo handler (eng oxirida turishi KERAK)
@router.message(StateFilter(None))
async def bot_echo(message: Message):
    await message.answer(message.text)
