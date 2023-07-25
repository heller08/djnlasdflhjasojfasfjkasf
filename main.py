import telebot
from telebot.apihelper import ApiTelegramException
from telebot import types
from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import os

bot = telebot.TeleBot('6127490151:AAHxsadq4VDWwA_wyz7awb1Z0hHkr7hZpA4')



fruit = 'https://clck.ru/356fe4'
mm2 = 'https://clck.ru/356fee'
adopt = 'https://clck.ru/356fde'
plsdonate = 'https://clck.ru/356fd8'
psx = 'https://clck.ru/356fcq'
helpos = 'http://t.me/killafied'

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ХОЧУ!")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Привет !\n\nЧтобы получить бесплатные вещи в режимах MM2, Adopt me, BloxFruit, Pls Donate нажми на ХОЧУ!\nУ нас есть отзывы!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "ХОЧУ!"):
        markup = InlineKeyboardMarkup()


        adopted = InlineKeyboardButton(text='Вип сервер ADOPT ME🐱', url=adopt)
        murdered = InlineKeyboardButton(text='Вип сервер MM2🔪', url=mm2)
        fruited = InlineKeyboardButton(text='Вип сервер Blox Fruit🍏', url=fruit)
        donated = InlineKeyboardButton(text='Вип сервер Pls Donate💸', url=plsdonate)
        pshhh = InlineKeyboardButton(text='Вип сервер Pet Simulator X🐱', url=psx)
        helposed = InlineKeyboardButton(text='Отзывы🥰', url=helpos)
        helped = InlineKeyboardButton(text='Помощь😀', callback_data='help_call')

        markup.add(adopted)
        markup.add(murdered)
        markup.add(fruited)
        markup.add(donated)
        markup.add(pshhh)
        markup.add(helposed, helped)

        bot.send_message(message.chat.id, """❤️Заходи на мои випки и там будут мои сотрудники, которым вы должны будете кинуть трейд❤️
❗️Вип на Adopt me, будет ждать сотрудник, который даст любого пета❗️
❗️Вип на ММ2 (нужен 10 лвл), будет ждать сотрудник, который даст любой нож и пистолет❗️
❗️Вип на Blox Fruit (нужно второе море), в трейде будет наш сотрудник который даст фрукты❗️
❗️Вип на PlsDonate, на сервере будет наш который задонатит от 100 до 500 робуксов❗️
😚Сотрудники работают круглосуточно😚""", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
    if req[0] == 'help_call':
        bot.send_message(call.message.chat.id, '@infinite_garant')



bot.polling(none_stop=True)