import telebot
bot = telebot.TeleBot("5820353314:AAG8Cy_ZI_mPpyBiQMY7i6QMWGUdw7H_CSI")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, f"Приветствую, {message.chat.username}")

# Обрабатывается все документы и аудиозаписи
@bot.message_handler()
def handle_start(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, "рад за вас")

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)