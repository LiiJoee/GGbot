import telebot

bot=telebot.TeleBot('5709307077:AAErb5ut5IKM7xHJh1LxncPB9bexG8DwVac')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет <b>{message.from_user.first_name } <u>{message.from_user.last_name}</u></b>'
    bot. send_message(message.chat.id, '<b>Hi</b>', parse_mode='html')


bot.polling(none_stop=True)