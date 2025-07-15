import telebot
import os

TOKEN = os.getenv("TOKEN")  # Получаем токен из переменных окружения

bot = telebot.TeleBot(TOKEN)
ADMIN_ID = 821932338  # Твой Telegram ID

@bot.message_handler(commands=["start"])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("📩 Оставить заявку")
    markup.add(item1)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!\nНажми кнопку ниже, чтобы оставить заявку.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📩 Оставить заявку")
def handle_request(message):
    bot.send_message(message.chat.id, "Введите вашу заявку:")
    bot.register_next_step_handler(message, forward_to_admin)

def forward_to_admin(message):
    text = f"🆕 Новая заявка от @{message.from_user.username or message.from_user.first_name}:\n\n{message.text}"
    bot.send_message(ADMIN_ID, text)
    bot.send_message(message.chat.id, "Ваша заявка отправлена. Мы с вами свяжемся!")

bot.polling(non_stop=True)
