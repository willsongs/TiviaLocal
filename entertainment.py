import telebot
import requests
import json
import math
from telebot import types


from telebot import custom_filters
from telebot import types

API_TOKEN = '5505287179:AAFu9iQ7jTeY8JM_KTN7hPe6oUawkYI195A'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    print(message.chat.id)
    try:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        bot.reply_to(message, 'okey! now enter any name of movie or webseries you want to watch today', reply_markup=markup)
    except Exception:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=["done"])
def done(message):
    name = message.text
    spltarray = name.split(" ",2)
    mv_name = spltarray[2]
    c_id = spltarray[1]
    try:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        bot.send_message(c_id, f'The movie has been added to the database 😊\n You can retry now\n try saying```{mv_name.strip()}```', parse_mode = 'MarkdownV2', reply_markup=markup)
    except Exception:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda message: message.text.lower() in ['ok'])
def ok(message):
    try:
        bot.reply_to(message, "😊", reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(regexp=r'\b[ a-zA-Z.]+\b')
def name(message):
    try:
        term = message.text
        u_id = message.from_user.id
        # print(term)
        url = requests.get(f"https://doodapi.com/api/search/videos?key=13527p8pcv54of4yjeryk&search_term={term}")
        data = url.text
        parse_json = json.loads(data)

        n = len(parse_json['result'])
        if n==0:
            bot.reply_to(message,'the movie is not in the database right now. Will be added to the database soon')
            bot.send_message(message.chat.id, 'Please try again after some time \n Wait for next 15 minutes and try again')
            bot.send_message(1915029649, f"```request {term}``` ```{u_id}```", parse_mode = 'MarkdownV2')

        else:
            for i in range(n):
                code = parse_json['result'][i]['file_code']
                img = parse_json['result'][i]['splash_img']
                name = parse_json['result'][i]['title']
                s_url = requests.get(f"https://doodapi.com/api/file/info?key=13527p8pcv54of4yjeryk&file_code={code}")
                sdata = s_url.text
                s_parse = json.loads(sdata)
                raw_size = s_parse['result'][0]['size']
                size = int(raw_size)
                if size == 0:
                    return "0B"
                size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
                i = int(math.floor(math.log(size, 1024)))
                p = math.pow(1024, i)
                s = round(size / p, 2)
                file_size = "%s %s" % (s, size_name[i])
                watch_link = f"https://dood.wf/d/{code}"
                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                btn1 = telebot.types.InlineKeyboardButton('Watch', url= watch_link, callback_data="click")
                markup.add(btn1)
                bot.send_photo(message.chat.id, img,f"<b>TITLE:</b> <i>{name}</i>\n"
                                                    f"\n<b>SIZE:</b> <i>{file_size}</i>\n", parse_mode = 'html',reply_markup = markup)

    except Exception:
        bot.reply_to(message, 'oooops')

bot.polling()
