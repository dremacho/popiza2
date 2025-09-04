from aiogram import Bot, Dispatcher
import asyncio

API_TOKEN = "YOUR_BOT_TOKEN"  # вставь свой токен телеграм-бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def main():
    print("Бот запущен")
    await bot.session.close()  # закрываем сессию, чтобы не было ошибок

if __name__ == "__main__":
    asyncio.run(main())
