import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ['token'])

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(massage):
    bot.send_message(message.chat.id, 'Alina dura, napishi poka')

@server.route('/', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

if __name__ == '__main__':
    server.run()