from aiogram import types, executor, Dispatcher, Bot
from aiogram.types.message import ContentType
import logging
import  random
import aiogram

#################TOKEN######################
logging.basicConfig(level=logging.INFO)
TOKEN = 'YOU BOT TOKEN'
############################################

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


#############NOMER##########################

l = list(range(1, 100))
random.shuffle(l)
for i in l:
    i
#############################################start##################

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await bot.send_sticker(message.chat.id, "YOU CHAT API")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Купить подписку", callback_data="random_value1"))
   # keyboard.add(types.InlineKeyboardButton(text="Аккаунты", callback_data="random_value2"))
    keyboard.add(types.InlineKeyboardButton(text="Продажа подписки", callback_data="random_value2"))
    keyboard.add(types.InlineKeyboardButton(text="Ссылка на проект в SberZ", url="https://newschool.sberclass.ru/accelerator/projects/38cf84b8-b027-4dac-bbb4-4ab64a47402c"))
    await bot.send_message(message.chat.id,
                           f"""❈ ═══════❖═══════ ❈
Здравствуйте {message.from_user.last_name} {message.from_user.first_name}!👋
Этот сервис для шаринга и продажи аккаунтов, подпискок .

Основные команды бота:
1)Запуск бота - /start 
2)Помощь - /help

Проект разработан для акселератора SberZ.

Обработчик заказов - https://t.me/i_share_obr
Если у вас возникли сложности прошу обращаться - https://t.me/iokitq""", reply_markup=keyboard)
    await bot.send_message(2010105481, f"{message}")
    print(1)

################################################################
@dp.message_handler(commands=["help"])
async def cmd_start(message: types.Message):
    keyboard2 = types.InlineKeyboardMarkup()
    await bot.send_message(message.chat.id ,f"""──────── • ✤ • ────────
Этот бот помогает людям делиться подписками.
 Если вам надо купить подписку нажмите 
'купить подписку', если вам надо разделить подписку нажмите 'продать подписку'.
Я считаю что каждый человек может поделиться с подпиской, таким образом он не только получает выгоду для себя, но и для других. Покупка и продажа происходит официально. 
Если у вас возникли вопросы, пожалуйста, пишите мне - https://t.me/iokitq. Спасибо всем за внимание. И будь немного добрей /start
──────── • ✤ • ────────""")


###############################################################
@dp.callback_query_handler(text="random_value1")
async def send_random_value(call: types.CallbackQuery):
    keyboard2 = types.InlineKeyboardMarkup()

    keyboard2.add(types.InlineKeyboardButton(text="Яндекс Плюс ----- 149 вместо 299 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="Иви ------------- 149 вместо 399 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="Genshin impact - 10 ранг - 30 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="Genshin impact - 17 ранг - 30 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="World of tanks | аккаунт 60 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="Ак вк авто - 30 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="Best spotify) - 30 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="Ipvanish vpn best top1 - 90 р", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))
    keyboard2.add(types.InlineKeyboardButton(text="", callback_data="value1"))



    await call.message.answer(text=f"""❈ ═══════❖═══════ ❈
Выберите интересующий вас подписку.
Подробности подписки можно узнать на официальном сайте.
Гарантия действует на момент покупки, если вы наткнулись на мошенника писать - https://t.me/iokitq.
──────── • ✤ • ────────""", reply_markup=keyboard2)
    print(2)
##################################################################

@dp.callback_query_handler(text="value1")


async def send_random_value(call: types.CallbackQuery):
    keyboard3 = types.InlineKeyboardMarkup()

    keyboard3.add(types.InlineKeyboardButton(text="Банковские карты ", url="https://www.tinkoff.ru/rm/minnullin.ayvaz1/1a5xA78974"))
    keyboard3.add(types.InlineKeyboardButton(text="ЮMoney",url="https://yoomoney.ru/to/4100118111799237"))
    keyboard3.add(types.InlineKeyboardButton(text="Далее", callback_data="pue1"))

    await call.message.answer(text=f"""     ⵈ━══════╗◊╔══════━ⵈ
Выберите удобный для вас способ оплаты.
Введите указанную стоимость подписки.
Важно при оплате указать номер заказа и подписку в комментариях.
Ваш номер заказа P - {i}.
""", reply_markup=keyboard3)
###########################################################
@dp.callback_query_handler(text="pue1")
async def send_random_value(call: types.CallbackQuery):

    keyboard3 = types.InlineKeyboardMarkup()
    keyboard3.add(types.InlineKeyboardButton(text="Сообщить номер заказа",url="https://t.me/i_share_obr"))

    await call.message.answer(text=f"""ⵈ━══════╗◊╔══════━ⵈ
Спасибо. Ваш заказ оплачен.
Важно: сообщить свой заказ обработчику(https://t.me/i_share_obr) 
после оплаты (если вы не сделаете это то мы не сможем отправить ссылку)""", reply_markup=keyboard3)



########################################
###########################
####################3



@dp.callback_query_handler(text="random_value2")
async def send_random_value(call: types.CallbackQuery):
    keyboard2 = types.InlineKeyboardMarkup()
    keyboard2.add(types.InlineKeyboardButton(text="Написать", url="https://t.me/i_share_obr"))
    await call.message.answer(text=f"""❈ ═══════❖═══════ ❈
Для того чтобы делиться подписками вы должны написать обработчик по такому шаблону: 
1)Ваш номер. 
2)Название подписки.
3)Период подписки.
5)Количество участников.
4)Цена на одного участника. 

Ваш номер R - {i}
──────── • ✤ • ────────""", reply_markup=keyboard2)



executor.start_polling(dp)


