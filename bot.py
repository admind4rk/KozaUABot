import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ['token'])

server = Flask{__name__}

@bot.message_handler(commands=['start'])
def send_welcome(massage):
    bot.send_message(message.chat.id, 'Alina dura, napishi poka')

@bot.message_handler(content_types=['text', 'document', 'audio'])

def get_text_messages(message)

if message.text == "poka":
    bot.send_message(message.from_user.id, "Privet. Chem ya mogu pomoch'?")
elif massage.text == "/help":
    bot.send_message(message.from_user.id, "napishi poka")
else:
    bot.send_message(message.from_user.id, "napishi poka")

@server.route('/', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

if __name__ == '__main__':
    server.run()