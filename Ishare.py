from aiogram import types, executor, Dispatcher, Bot
from aiogram.types.message import ContentType
import logging
import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = '5784301297:AAFjUKkl_sRPuNWWrwrS0FIm4U5WduOmS3U'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

i = random.randint(30,50)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHslVj6JnhzW68_HJ4G-g9JB-lDe8qjQAC_Q8AAoqi0EmT6eEEbPSFWC4E")

    sell_button = InlineKeyboardButton(text="Продажа подписки💰", callback_data='random_value2')
    buy_button = InlineKeyboardButton(text="Купить подписку💳", callback_data='random_value1')
    keyboard = InlineKeyboardMarkup().add(sell_button, buy_button)

    #keyboard.add(types.InlineKeyboardButton(text="Правила 📝",url="https://t.me/iokitq"))
    #keyboard.add(types.InlineKeyboardButton(text="Наш сайт 💻", url="https://t.me/iokitq"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь 🤝", url="https://t.me/iokitq"))
    keyboard.add(types.InlineKeyboardButton(text="Ссылка на проект в SberZ", url="https://newschool.sberclass.ru/accelerator/projects/38cf84b8-b027-4dac-bbb4-4ab64a47402c"))
    await bot.send_message(message.chat.id,
                           f"""
Здравствуйте {message.from_user.last_name} {message.from_user.first_name}!👋
Этот сервис для шеринга подписок.

Проект разработан для акселератора SberZ.

Обработчик заказов - https://t.me/i_share_obr
Если у вас возникли сложности прошу обращаться - https://t.me/iokitq""", reply_markup=keyboard)
    print(message)


@dp.callback_query_handler(text="random_value1")
async def send_random_value(call: types.CallbackQuery):
    keyboard2 = types.InlineKeyboardMarkup()

    keyboard2.add(types.InlineKeyboardButton(text="Яндекс Плюс ----- 149 вместо 299 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="Иви ------------- 149 вместо 399 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text=f"""Облачный гейминг - от 13 руб/час.""", callback_data="value5"))
    keyboard2.add(types.InlineKeyboardButton(text=f"""okko лайт-доп.устройство-49 руб вместо 199""", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text=f"""оkkо оптимум-доп.устройство-69 руб""", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text=f"""оkkо оптимум + спорт - 199 руб вместо 499""", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text=f"""Mybook premium - 3 мес- 299""", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text=f"""Spotify - 1 мес - 169 руб""", callback_data="value1"))

    await call.message.answer(text=f"""
Выберите интересующий вас подписку.
Подробности подписки можно узнать на официальном сайте.
Гарантия действует на момент покупки, если вы наткнулись на мошенника писать - https://t.me/iokitq.
""", reply_markup=keyboard2)

@dp.callback_query_handler(text="value5")

async def send_random_value(call: types.CallbackQuery):
    keyboard3 = types.InlineKeyboardMarkup()
    keyboard3.add(types.InlineKeyboardButton(text="Сообщить номер заказа", url="https://t.me/i_share_obr"))

    await call.message.answer(text=f"""
Играйте по самой низкой цене от 13 руб час. Для этого напишите нашему обработчику номер заказа и название игры. 
Ваш номер заказа P - {i}.
""", reply_markup=keyboard3)

@dp.callback_query_handler(text = "value1")

async def send_random_value(call: types.CallbackQuery):
    keyboard3 = types.InlineKeyboardMarkup()
    keyboard3.add(types.InlineKeyboardButton(text="Банковские карты ", url="https://www.tinkoff.ru/rm/minnullin.ayvaz1/1a5xA78974"))
    keyboard3.add(types.InlineKeyboardButton(text="ЮMoney",url="https://yoomoney.ru/to/4100118111799237"))
    keyboard3.add(types.InlineKeyboardButton(text="Далее", callback_data="pue1"))
    await call.message.answer(text=f""" 
Выберите удобный для вас способ оплаты.
Введите указанную стоимость подписки.
Важно при оплате указать номер заказа и подписку в комментариях.
Ваш номер заказа P - {i}.
""", reply_markup=keyboard3)
###########################################################
@dp.callback_query_handler(text="pue1")
async def send_random_value(call: types.CallbackQuery):
    keyboard3 = types.InlineKeyboardMarkup()
    await call.message.answer(text=f"""
Спасибо. Ваш заказ оплачен.
Важно: сообщить свой заказ обработчику(https://t.me/i_share_obr) 
после оплаты (если вы не сделаете это то мы не сможем отправить ссылку)""", reply_markup=keyboard3)

@dp.callback_query_handler(text="random_value2")
async def send_random_value(call: types.CallbackQuery):
    keyboard2 = types.InlineKeyboardMarkup()
    keyboard2.add(types.InlineKeyboardButton(text="Написать", url="https://t.me/i_share_obr"))
    await call.message.answer(text=f"""
Для того чтобы делиться подписками вы должны написать обработчик по такому шаблону: 
1)Ваш номер. 
2)Название подписки.
3)Период подписки.
5)Количество участников.
4)Цена на одного участника. 

Ваш номер R - {i}""", reply_markup=keyboard2)

executor.start_polling(dp, skip_updates=False)


