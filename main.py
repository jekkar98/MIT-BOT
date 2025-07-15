import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
USER_ID = os.getenv("USER_ID")  # Убираем принудительное преобразование в int

if not USER_ID:
    raise ValueError("Переменная USER_ID не задана")

try:
    USER_ID = int(USER_ID)
except ValueError:
    raise ValueError("USER_ID должен быть числом")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привет! Я бот для обработки заявок. Напишите 'заявка', чтобы оставить заявку.")

@dp.message_handler(lambda message: message.text.lower() in ["оставить заявку", "заявка"])
async def handle_request(message: types.Message):
    username = message.from_user.username or 'без ника'
    await bot.send_message(USER_ID, f"Новая заявка от @{username}:\n{message.text}")
    await message.answer("Заявка отправлена! Мы скоро свяжемся с вами.")

async def main():
    print("Бот запущен...")
    await dp.start_polling()

if __name__ == "__main__":
    from aiogram import executor
    executor.start(main())
