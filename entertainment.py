import telebot
import requests
import json
import math
from telebot import types
import multiprocessing
from datetime import datetime, timedelta
from telebot import custom_filters
from telebot import types

# testing by wahid:
# API_TOKEN = '5505287179:AAFu9iQ7jTeY8JM_KTN7hPe6oUawkYI195A'

# local testing:
API_TOKEN = '5620400281:AAHw03yvbtfCpitTWl_r3RXlSACHgeL2IPg'


bot = telebot.TeleBot(API_TOKEN)

user_dict = {}

session  = requests.session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko)'
    'Chrome?58.0.3029.110 Safari/537.3'})
class User:
    def __init__(self,u_id):
        self.u_id = u_id

@bot.message_handler(commands=["start"])
def start(message):
    print(message.chat.id)
    try:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        bot.reply_to(message, 'okey! now enter any name of movie or webseries you want to watch today',
                     reply_markup=markup)
    except Exception:
        bot.reply_to(message, 'oooops')

@bot.message_handler(commands=['broadcast'])
def inptmsg(message):
    try:
        msg = bot.send_message(message.chat.id, "ok. forward the message")
        bot.register_next_step_handler(msg, brdcst)
    except:
        bot.send_message(message.chat.id, "something went wrong")

def brdcst(message):
    li = [2086643719, 650526737, 5412171798, 2038568986, 771104798, 1401487394, 2115387437, 5406912558, 5321390130, 490944563, 847065157, 5628694607, 1054425172, 1247244376, 1267757157, 1248465004, 1101027437, 1655144559, 1915029649, 697915541, 1475965084, 1120870562, 2125181093, 641706152, 1437122138, 1343926441, 5201195176, 640782547, 1118116085, 1435912450, 1981280551, 5576388904, 5713416505, 1726406986, 5581549913, 5238417770, 424702316, 5771962740, 973101443, 977457540, 343603589, 5674131852, 1255102869, 1967663517, 1087365534, 1462913441, 1061046696, 359068078, 1918792133, 574640583, 510634455, 1820774871, 1246693853, 722846193, 5527331323, 1256354327, 630141507, 5473604165, 1056201309, 1285773924, 1444676211, 1628340858, 982373001, 471159435, 5528023700, 5274542741, 1934545564, 5736026781, 5282304671, 1840503457, 5736680105, 5396751043, 1460234962, 933323488, 1895756519, 1821434609, 2139099915, 5238782735, 1297124119, 5331522339, 731956003, 1943296815, 1299591995, 1390644043, 430545756, 1468584801, 1164385133, 5391719303, 5790190484, 5311226797, 2084510643, 5569969079, 2135346108, 1857729473, 641926083, 5192344517, 5379683287, 5003559897, 1228141528, 1679915995, 1322806235, 5689000937, 5312674815, 782687241, 1802443787, 681776143, 1820167186, 1768203298, 1267741731, 1838896166, 5736381493, 929901638, 1609858119, 933784663, 1161462874, 5525517403, 890649706, 1676205165, 694568077, 5030063249, 5354091675, 5733762210, 780700835, 1281346725, 759370926, 855203002, 1701541060, 987720913, 1317604562, 5466305749, 5745229013, 778702037, 5341908195, 1301048550, 1731560683, 829990126, 987346159, 5209816313, 5446995254, 1362953170, 5373613372, 1352537408, 5821943120, 903064914, 5193973136, 1705196959, 1638450592, 834321831, 638487981, 582935998, 1411417547, 5430531562, 972666367, 5709092351, 576722445, 1325671955, 902090266, 2136598054, 702619189, 2017951293, 1551302223, 5771642460, 1415976541, 1361747557, 774510189, 1954027121, 1674153587, 5310910092, 5517354647, 855084704, 775003809, 5007693478, 1346647726, 555386549, 5500839609, 1086658235, 5794422483, 5358556886, 2017431256, 523431652, 653854437, 1966794472, 870708970, 1078718189, 5329135343, 5383866115, 5007888132, 5050343178, 1143265036, 633917199, 5354372910, 5110597457, 1232121686, 599810758, 863108978, 1482579830, 1053366138, 2023399292, 1248608128, 1468585856, 785244035, 5077598105, 5104535482, 660922340, 982530027, 5196748789]
    # li = [1915029649, 2073000480]
    from_chat_id = 1915029649
    ids = len(li)
    for i in range (ids):
        try:
            chat_id = li[i]
            bot.forward_message(chat_id, from_chat_id, message.message_id)
            bot.send_message(message.chat.id, f"send successfully to {chat_id}")
        except:
            bot.send_message(message.chat.id, 'something went wrong')
            bot.send_message(message.chat.id, f"{chat_id} left bot")


@bot.message_handler(commands=["done"])
def done(message):
    name = message.text
    spltarray = name.split(" ", 2)
    mv_name = spltarray[2]
    c_id = spltarray[1]
    try:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        bot.send_message(c_id,
                         f'The movie has been added to the database 😊\n You can retry now\n try saying```{mv_name.strip()}```',
                         parse_mode='MarkdownV2', reply_markup=markup)
    except Exception:
        bot.reply_to(message, 'oooops')


@bot.message_handler(func=lambda message: message.text.lower() in ['ok'])
def ok(message):
    try:
        bot.reply_to(message, "😊")
    except Exception as e:
        bot.reply_to(message, 'oooops')

def fetch_final_data(code):
    s_url = requests.get(f"https://doodapi.com/api/file/info?key=13527p8pcv54of4yjeryk&file_code={code}")
    sdata = s_url.text
    s_parse = json.loads(sdata)
    img = s_parse['result'][0]['splash_img']
    name = s_parse['result'][0]['title']
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
    watch_link1 = f"https://dood.re/d/{code}"
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    btn1 = telebot.types.InlineKeyboardButton('Watch', url=watch_link, callback_data="click")
    btn2 = telebot.types.InlineKeyboardButton('alternate link', url=watch_link1)
    markup.add(btn1, btn2)
    return img, name, file_size, markup

@bot.message_handler(regexp=r'\b[ a-zA-Z.]+\b')
def name(message):
    try:
        term = message.text
        u_id = message.from_user.id
        print(term)
        url = requests.get(f"https://doodapi.com/api/search/videos?key=13527p8pcv54of4yjeryk&search_term={term}")
        data = url.text
        
        #set cache
        now = datetime.now()
        expires_at = now + timedelta(hours=1)  # Cache for 1 hour
        session.headers.update({
            'Cache-Control': 'public, max-age=3600',
            'Expires': expires_at.strftime('%a, %d %b %Y %H:%M:%S GMT')
        })
        
        parse_json = json.loads(data)
        # make a list of all the filecodes
        res = parse_json["result"]
        key = "file_code"
        f_codes = [d.get(key) for d in res]

        n = len(parse_json['result'])
        if n == 0:
            bot.reply_to(message, 'the movie is not in the database right now. Will be added to the database soon')
            bot.send_message(message.chat.id,
                             'Please try again after some time \n Wait for next 15 minutes and try again')

            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('done default', callback_data="done_default")
            btn2 = telebot.types.InlineKeyboardButton('done custom', callback_data= 'done_custom')
            markup.add(btn1,btn2)
            bot.send_message(1915029649, f"```request {term}```,```{u_id}```", parse_mode='MarkdownV2',
                             reply_markup=markup)

        else:
            # we will add the list of all file codes here/
            try:
                if __name__ == "__main__":
                    with multiprocessing.Pool(processes=4) as pool:
                        main_data = pool.map(fetch_final_data, f_codes)
                        for img, name, file_size, markup in main_data:
                            bot.send_photo(message.chat.id, img, f"<b>TITLE:</b> <i>{name}</i>\n"
                                                     f"\n<b>SIZE:</b> <i>{file_size}</i>\n", parse_mode='html',
                                    reply_markup=markup)
            except:
                pass

    except Exception:
        bot.reply_to(message, 'oooops')

@bot.callback_query_handler(func=lambda c: c.data == 'click')
def click(call: types.CallbackQuery):
    try:
        print(call.message.chat.id)
    except Exception:
        print("something went wrong")


@bot.callback_query_handler(func=lambda c: c.data == 'done_default')
def done_default(call: types.CallbackQuery):
    c_id = call.message.chat.id
    raw_text = call.message.text
    txtsplt = raw_text.split(',')
    u_id = txtsplt[1]
    print(u_id)
    mv_name = txtsplt[0]
    try:
        # print(f"{mv_name} & {u_id}")
        bot.send_message(u_id.strip(),
                         f"The movie has been added to the database 😊\nYou can retry now\nTry saying```waste {mv_name.strip()}```",
                         parse_mode="Markdownv2")
        bot.send_message(1915029649, "message sent successfully ")
    except Exception:
        print("something went wrong")
        bot.send_message(1915029649, "kuch glt ho gaya :(")

@bot.callback_query_handler(func=lambda c: c.data == 'done_custom')
def done_custom(call: types.CallbackQuery):
    c_id = call.message.chat.id
    raw_text = call.message.text
    txtsplt = raw_text.split(',')
    u_id = txtsplt[1]
    print(u_id)
    user = User(u_id)
    user_dict[c_id] = user
    # mv_name = txtsplt[0]
    try:
        # print(f"{mv_name} & {u_id}")
        msg = bot.send_message(c_id, "Enter correct name")
        bot.register_next_step_handler(msg, crct_name)
    except Exception:
        print("something went wrong")
        bot.send_message(1915029649, "kuch glt ho gaya :(")

def crct_name(message):
    chat_id = message.chat.id
    mv_name = message.text
    user = user_dict[chat_id]

    try:
        bot.send_message(user.u_id.strip(),
                         f"The movie has been added to the database 😊\nYou can retry now\nTry saying```waste {mv_name.strip()}```",
                         parse_mode="Markdownv2")
        bot.send_message(1915029649, "message sent successfully ")
    except Exception:
        print("something went wrong")
        bot.send_message(1915029649, "kuch glt ho gaya :(")

bot.enable_save_next_step_handlers(delay=2)

# bot.load_next_step_handlers()

bot.polling()
