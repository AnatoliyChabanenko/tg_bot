import telebot
import config
from telebot import types
import json


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(massege):
    sti = open('static/AnimatedSticker.tgs', 'rb')
    bot.send_animation(massege.chat.id, sti)

    # клавав
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Пшениця 2-го класу')
    item2 = types.KeyboardButton('Пшениця 3-го класу')
    item3 = types.KeyboardButton('Пшениця 4-го класу')
    item4 = types.KeyboardButton('Ячмінь')
    item5 = types.KeyboardButton('Кукурудза')
    item6 = types.KeyboardButton('Соняшник')
    markup.add(item1,item2,item3,item4,item5,item6)



    bot.send_message(massege.chat.id, 'Доброго времени суток ',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lala(massege):
    if massege.chat.type == 'private':
        data = json.load(open('data.json'))

        if massege.text == 'Пшениця 2-го класу':
            bot.send_message(massege.chat.id , data['1'] )

        elif massege.text == 'Пшениця 3-го класу':
            bot.send_message(massege.chat.id , data['2'] )


        elif massege.text == 'Пшениця 4-го класу':
            bot.send_message(massege.chat.id , data['3'] )

        elif massege.text == 'Ячмінь':
            bot.send_message(massege.chat.id , data['4'] )

        elif massege.text == 'Кукурудза':
            bot.send_message(massege.chat.id , data['5'] )

        elif massege.text == 'Соняшник':
            bot.send_message(massege.chat.id ,data['6'] )



bot.polling(none_stop=True)

