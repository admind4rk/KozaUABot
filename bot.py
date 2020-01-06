import os
import telebot;

bot = telebot.TeleBot(os.environ['token'])

server = Flask{__name__}

@bot.massage_handler(commands=['start'])
def send_welcome(massage):
    bot.send_massage(massage.chat.id, 'PRIVETTTTTTT')

@bot.massage_handler(content_types=['text', 'document', 'audio'])

def get_text_massages(message)

if massage.text == "Privet":
    bot.send_massage(massage.from_user.id, "Privet. Chem ya mogu pomoch'?")
elif massage.text == "/help":
    bot.send_massage(massage.from_user.id, "Napishi privet")
else:
    bot.send_massage(massage.from_user.id, "Ya tebya ne ponimayu")

bot.polling(none_stop=True, interval=0)