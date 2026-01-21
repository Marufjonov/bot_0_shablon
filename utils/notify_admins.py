from data.config import ADMINS

async def on_startup_notify(bot):
    for admin_id in ADMINS:
        try:
            await bot.send_message(
                admin_id,
                "✅ Bot ishga tushdi!"
            )
        except Exception:
            pass
