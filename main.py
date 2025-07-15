
import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Добро пожаловать в MT-IT бот!\nВыберите действие ниже.")

@dp.message_handler(lambda message: message.text.lower() in ["оставить заявку", "заявка"])
async def handle_request(message: types.Message):
    user_id = 821932338  # Твой Telegram ID
    await bot.send_message(user_id, f"📩 Новая заявка от @{message.from_user.username or 'без ника'}:\n{message.text}")
    await message.answer("✅ Заявка отправлена! Мы скоро свяжемся с вами.")

if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)
