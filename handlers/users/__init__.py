from aiogram import Router

from .start import router as start_router
from .help import router as help_router   # keyin qo‘shasiz
from .echo import router as echo_router
from .commandFilters import router as til_router
from .contenthandlers import router as content_router


router = Router()
router.include_router(start_router)
router.include_router(help_router)
router.include_router(til_router)
router.include_router(content_router)
router.include_router(echo_router)  # 🔥 ENG OXIRIDA

