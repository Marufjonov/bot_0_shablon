from aiogram import Router
from handlers.users import router as users_router

router = Router()
router.include_router(users_router)
