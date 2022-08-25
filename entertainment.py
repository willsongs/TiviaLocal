import telebot
import requests
import json

from telebot import custom_filters
from telebot import types

API_TOKEN = '5505287179:AAFu9iQ7jTeY8JM_KTN7hPe6oUawkYI195A'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    try:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        bot.reply_to(message, 'okey! now enter any name of movie or webseries you want to watch today', reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(regexp=r'\b[ a-zA-Z.]+\b')
def input(message):
    try:
        term = message.text
        # print(term)
        url = requests.get(f"https://doodapi.com/api/search/videos?key=13527p8pcv54of4yjeryk&search_term={term}")
        data = url.text
        parse_json = json.loads(data)

        n = len(parse_json['result'])
        if n==0:
            bot.reply_to(message,'the movie is not in the database right now. Will be added to the database soon')
            bot.send_message(message.chat.id, 'Please try again after some time \n Wait for next 15 minutes and try again')
            bot.send_message(1915029649, msg.text)

        else:
            for i in range(n):
                # print(parse_json['result'][i])
                code = parse_json['result'][i]['file_code']
                img = parse_json['result'][i]['splash_img']
                name = parse_json['result'][i]['title']
                # print(f"https://dood.wf/d/{code}")
                # print(img)
                bot.send_photo(message.chat.id, img, f"TITLE: {name}\n\nhttps://dood.wf/d/{code}")

    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(commands=["Ok thanks","thank you","thnx"])
def start(message):
    try:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        bot.reply_to(message, 'My pleasure 😊', reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')


bot.polling()
