import logging
import time
import telebot

# Инициализация бота
API_TOKEN = "7205433194:AAHc-N7ApUxtZU0w7zdVpj1GthE-o4pRnXk"
bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я финансовый бот. Отправь мне сумму вклада и срок, и я рассчитаю проценты.")

@bot.message_handler(func=lambda message: message.text.isdigit())
def calculate_deposit(message):
    try:
        # Получаем сумму вклада и срок
        deposit_amount = float(message.text)
        deposit_term = 12  # Предполагаем, что вклад на 12 месяцев

        # Примерный расчет процентов (5% годовых)
        interest_rate = 0.05
        total_interest = deposit_amount * interest_rate * (deposit_term / 12)

        bot.reply_to(message, f"При вкладе {deposit_amount:.2f} на {deposit_term} месяцев, "
                              f"вы получите примерно {total_interest:.2f} процентов дохода.")
    except ValueError:
        bot.reply_to(message, "Неверный формат данных. Пожалуйста, введите сумму вклада (например, '10000').")

if __name__ == '__main__':
    bot.polling(none_stop=True)
