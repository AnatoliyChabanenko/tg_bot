import  config2
import logging

from  sqlighter import SQLighter
from aiogram import Bot , Dispatcher ,executor , types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(level=logging.INFO)

#инитицеализация бота
bot = Bot(token= config2.TOKEN)
dp = Dispatcher(bot)

db = SQLighter('db.db')


button_hi = KeyboardButton('Привет! 👋')

button1 = KeyboardButton('1')
button2 = KeyboardButton('2')
button3 = KeyboardButton('3')

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4')
button5 = KeyboardButton('5')
button6 = KeyboardButton('/geo')
markup5.row(button4, button5)
markup5.insert(button6)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию', request_location=True)
)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=markup5)

@dp.message_handler(commands=['geo'])
async def process_hi6_command(message: types.Message):
    await message.reply("Шестое - запрашиваем контакт и геолокацию\nЭти две кнопки не зависят друг от друга", reply_markup=markup_request)

#активация
@dp.message_handler(commands=['subscribe'])
async def subscribe(massage: types.Message):
    if( not  db.subscriber_exists(massage.from_user.id)):
        db.add_subscriber(massage.from_user.id)
    else:
        db.update_subscription(massage.from_user.id, True)

        await massage.answer('отлично')


@dp.message_handler(commands=['unsubscribe'])
async def subscribe(massage: types.Message):
    if( not  db.subscriber_exists(massage.from_user.id)):
        db.add_subscriber(massage.from_user.id, False)
        await massage.answer('Вы и так не пописаны.')
    else:
        db.update_subscription(massage.from_user.id, False)

        await massage.answer('Вы успешно отписались ')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)


