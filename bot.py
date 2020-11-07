import telebot

import os



bot = telebot.TeleBot('1499050063:AAFcWmtkRPoOIfGECwme0VpJvARZywMYD3s')



@bot.message_handler(content_types=['text'])

def send_text(message):

    if message.text == 'Hi':

         bot.send_message(message.chat.id, 'Hello')



    elif message.text == 'Who is your creatore?':
        bot.send_message(message.chat.id, 'Your name')


    else:
        atext = message.text[:3] + message.text.lower()
        bot.send_message(message.chat.id, atext)

bot.polling()