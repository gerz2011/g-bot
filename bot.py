import os
import telebot
import math
from telebot import apihelper
from telebot import types
from data import price_iphone_x
from data import price_iphone_8
from data import price_iphone_7
from data import price_ipad


TOKEN = '781098537:AAEGQ7-kRv6Pt8KGs5CfW9RiPRLU8lKHp58'
bot = telebot.TeleBot(TOKEN)


# apihelper.proxy = {'https':'https://188.216.77.95:8118'}

main_menu = 'iphone_ipad_wath_macbook_Наши контакты'.split('_')

problem_x = 'Дисплей ориг_Замена стекла_Заднее стекло_Аккумулятор_Защитное стекло'.split('_')
problem_8 = 'Дисплей ориг_Замена стекла_Заднее стекло_Копия ААА_Аккумулятор_Защитное стекло'.split('_')
problem_7 = 'Дисплей ориг_Замена стекла_Копия ААА_Аккумулятор_Защитное стекло'.split('_')
problem_ipad = 'Замена стекла_Замена модуля'.split('_')

iphone = 'Xs Max_Xs_Xr_X_8 Plus_8_7 Plus_7_6s Plus_6s_6 Plus_6_SE_5 серия'.split('_')

ipad = list(price_ipad)

contact = f'Выездной ремонт iPhone "PROFIPHONE"\nтел: 8 931 340 38 33\nтел: 8 (812) 648-59-51\nадес: м. Сенная, Московский пр. д2'


def text_massage(model, price_iphone):
    if price_iphone == price_iphone_x: problem = problem_x
    if price_iphone == price_iphone_8: problem = problem_8
    if price_iphone == price_iphone_7: problem = problem_7
    if price_iphone == price_ipad: problem = problem_ipad
    num = 0
    massage = []
    for key in price_iphone[model]:
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
        for iter in range(math.ceil(len(i) / 4)):
            array.append(i[w:w+4])

            w = w + 4
    for i in array:
        markup.row(*[types.KeyboardButton(name) for name in i])
    return markup


@bot.message_handler(commands=['start'])
def get_id(m):
    mt = app_btn([main_menu])
    bot.send_message(m.from_user.id, "выберите устройство:", reply_markup=mt)
    

@bot.message_handler(content_types=['text'])
def answe(m):

    if m.text == 'назад':
        mt = types.ReplyKeyboardRemove()
        bot.send_message(m.from_user.id, "назад", reply_markup=mt)
        mt = app_btn([main_menu])
        bot.send_message(m.from_user.id, "выберите устройство:", reply_markup=mt)
    if m.text == 'Наши контакты':
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
    # if m.text == 'wach':
    #     mt = app_btn([wach])
    #     mt.row(types.KeyboardButton('назад'))
    #     bot.send_message(m.from_user.id, "выберите модель:", reply_markup=mt)
    # if m.text == 'macbook':
    #     mt = app_btn([macbook])
    #     mt.row(types.KeyboardButton('назад'))
    #     bot.send_message(m.from_user.id, "выберите модель:", reply_markup=mt)

###############################################################################
##прайс с ценами
    if m.text in price_iphone_x:
        bot.send_message(m.from_user.id, text_massage(m.text, price_iphone_x))
        print(m.text)
    if m.text in price_iphone_8:
        bot.send_message(m.from_user.id, text_massage(m.text, price_iphone_8))
        print(m.text)
    if m.text in price_iphone_7:
        bot.send_message(m.from_user.id, text_massage(m.text, price_iphone_7))
        print(m.text)
    if m.text in price_ipad:
        bot.send_message(m.from_user.id, text_massage(m.text, price_ipad))
        print(m.text)




bot.polling()
