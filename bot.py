import os
from flask import Flask, request
import telebot
from telebot import apihelper
from telebot import types
from data import price_iphone
from data import price_ipad

server = Flask(__name__)

TOKEN = '781098537:AAEGQ7-kRv6Pt8KGs5CfW9RiPRLU8lKHp58'
bot = telebot.TeleBot(TOKEN)


apihelper.proxy = {'https':'https://188.216.77.95:8118'}

model = 'iphone_ipad_wath_macbook'.split('_')
link = 'Мы на крте_Контакты_Чат'.split('_')
problem = 'Дисплей ориг_Замена стекла_Копия ААА_Аккумулятор_Защитное стекло'.split('_')
iphone = list(price_iphone)
ipad = list(price_ipad)

contact = f'Выездной ремонт iPhone "PROFIPHONE"\nтел: 8 931 340 38 33\nтел: 8 (812) 648-59-51\nадес: м. Сенная, Московский пр. д2'


def text_massage(model, cl):
    num = 0
    massage = []
    for key in cl[model]:
        massage.append(f'{problem[num]} - {key} руб.\n')
        num = num + 1
    massage.append('---\nтел - 89313403833\nТелеграм - @gerz_og')
    massage = ' '.join(massage)
    return massage


def app_btn(arr):
    markup = types.ReplyKeyboardMarkup(True)
    array = []
    for i in arr:
        w = 0
        for iter in range(round(len(i) / 4)):
            array.append(i[w:w+4])
            w = w + 4
    for i in array:
        markup.row(*[types.KeyboardButton(name) for name in i])
    return markup


@bot.message_handler(commands=['start'])
def get_id(m):
    mt = app_btn([model, link])
    bot.send_message(m.from_user.id, "выберите устройство:", reply_markup=mt)
    

@bot.message_handler(content_types=['text'])
def answe(m):

    if m.text == 'назад':
        mt = types.ReplyKeyboardRemove()
        bot.send_message(m.from_user.id, "назад", reply_markup=mt)
        mt = app_btn([model, link])
        bot.send_message(m.from_user.id, "выберите устройство:", reply_markup=mt)
    if m.text == 'Контакты':
        mt = types.ReplyKeyboardRemove()
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='Наш официальный сайт', url='https://profiphone.ru/')
        btn_my_vk= types.InlineKeyboardButton(text='Группа Вконтакте', url='https://vk.com/yablonya_spb/')
        btn_my_insta= types.InlineKeyboardButton(text='Наш Instagram', url='https://www.instagram.com/iglass_spb/')
        btn_my_tg= types.InlineKeyboardButton(text='Напишите нам в телеграмм', url='https://t.me/gerz_og')
        btn_my_ya_map= types.InlineKeyboardButton(text='Мы на Яндекс карте', url='https://yandex.ru/maps/-/CCG7UM8c')
        markup.row(btn_my_site)
        markup.row(btn_my_tg)
        markup.row(btn_my_vk, btn_my_insta)
        markup.row(btn_my_ya_map)
        
        bot.send_message(m.from_user.id, contact, reply_markup = markup)
        
    

    if m.text == 'iphone':
        mt = app_btn([iphone])
        mt.row(types.KeyboardButton('назад'))
        bot.send_message(m.from_user.id, "выберите модель:", reply_markup=mt)
    if m.text == 'ipad':
        mt = app_btn([ipad])
        mt.row(types.KeyboardButton('назад'))
        bot.send_message(m.from_user.id, "выберите модель:", reply_markup=mt)
    if m.text == 'wach':
        mt = app_btn([ipad])
        mt.row(types.KeyboardButton('назад'))
        bot.send_message(m.from_user.id, "выберите модель:", reply_markup=mt)
    if m.text == 'macbook':
        mt = app_btn([ipad])
        mt.row(types.KeyboardButton('назад'))
        bot.send_message(m.from_user.id, "выберите модель:", reply_markup=mt)

###############################################################################
##прайс с ценами
    if m.text in price_iphone:
        bot.send_message(m.from_user.id, text_massage(m.text, price_iphone))
    if m.text in price_ipad:
        bot.send_message(m.from_user.id, text_massage(m.text, price_ipad))
    else: print('no price')



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://g-bot-1.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

        


         
    
    


bot.polling()