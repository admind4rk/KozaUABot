import telebot
from telebot import types
from telebot import apihelper

apihelper.proxy = {'http':'socks5://426209941:2dpVwJ2h@orbtl.s5.opennetwork.cc:999'}
bot = telebot.TeleBot('843317831:AAEAlRbKZTNcIjcSvFb1rq_Lbtv7Qtei4og')
#os.environ['token']
#843317831:AAEAlRbKZTNcIjcSvFb1rq_Lbtv7Qtei4og

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Аня, я в шоке с тебя, напиши привет')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Пиздец ты тупой(ая)")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "При":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True)