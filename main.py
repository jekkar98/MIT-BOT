import os
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем токен и ID
TOKEN = os.getenv("TOKEN")
USER_ID = os.getenv("USER_ID")

# Проверяем наличие необходимых переменных
if not TOKEN:
    raise ValueError("Не указан TOKEN в переменных окружения")
if not USER_ID:
    raise ValueError("Не указан USER_ID в переменных окружения")

try:
    USER_ID = int(USER_ID)
except ValueError:
    raise ValueError("USER_ID должен быть числом")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот для обработки заявок. Напишите 'заявка', чтобы оставить заявку.")

# Обработчик сообщений с заявками
@router.message(lambda message: message.text.lower() in ["оставить заявку", "заявка"])
async def handle_request(message: types.Message):
    username = message.from_user.username or 'без ника'
    try:
        await bot.send_message(USER_ID, f"Новая заявка от @{username}:\n{message.text}")
        await message.answer("Заявка отправлена! Мы скоро свяжемся с вами.")
    except Exception as e:
        await message.answer("Произошла ошибка при отправке заявки. Попробуйте позже.")

# Функция запуска
async def main():
    print("Бот запущен...")
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    from aiogram import executor
    executor.start(main())
