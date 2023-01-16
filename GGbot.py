import telebot

bot=telebot.TeleBot('5709307077:AAErb5ut5IKM7xHJh1LxncPB9bexG8DwVac')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name } <u>{message.from_user.last_name}</u></b>'
    bot. send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Твой <b>ID</b>: {message.from_user.id}", parse_mode='html')
    elif message.text == 'photo':
        photo = open('i_s.jpg', 'rb')
        bot.send_message(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, f'<b>Я тебя не понимаю</b>', parse_mode='html')




bot.polling(none_stop=True)