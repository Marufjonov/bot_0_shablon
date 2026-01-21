from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import Message, ContentType

router = Router()

# F.text
# F.photo
# F.video
# F.document
# F.audio
# F.voice
# F.location
# F.contact
# F.sticker
# F.caption
# F.data

@router.message(F.photo)
async def handle_photo(message: Message):
    await message.answer("📸 Rasm qabul qilindi")

@router.message(lambda m: m.content_type == ContentType.VIDEO)
async def handle_photo(message: Message):
    await message.answer("📸 Video qabul qilindi")