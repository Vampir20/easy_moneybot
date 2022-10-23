from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, CallbackQuery

TOKEN = "5735889826:AAFJbndUABrZcm5bwwSIM6nZpAlXOKMmtGU"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

amount_balance = 0


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    zarabotat = KeyboardButton(text="/earn")
    balance = KeyboardButton(text="/balance")
    support = KeyboardButton(text="/support")
    feedback = KeyboardButton(text="/feedback")
    markup.add(zarabotat, balance, support, feedback)
    await bot.send_message(message.from_user.id, "💰 Выберите способ заработка:", reply_markup=markup)


@dp.message_handler(commands=["earn"])
async def earn_money(message: types.Message):
    earn_kb = ReplyKeyboardMarkup(row_width=3)
    ikb1 = KeyboardButton(text="/Подписка на инстаграм-1грн", callback_data="btn1")
    ikb2 = KeyboardButton(text="/Подписка на инстаграм-1грн", callback_data="btn2")
    ikb3 = KeyboardButton(text="/Подписка на инстаграм-1грн", callback_data="btn3")
    ikb4 = KeyboardButton(text="/Подписка на канал-3грн", callback_data="btn4")
    ikb5 = KeyboardButton(text="/Подписка на канал-3грн", callback_data="btn5")
    ikb6 = KeyboardButton(text="/Подписка на канал-3грн", callback_data="btn6")
    ikb7 = KeyboardButton(text="/Подписка на канал-3грн", callback_data="btn7")
    ikb8 = KeyboardButton(text="/Подписка на канал-3грн", callback_data="btn8")
    ikb9 = KeyboardButton(text="/Пригласить друга-8грн", callback_data="btn9")

    earn_kb.add(ikb1, ikb2, ikb3, ikb4, ikb5, ikb6, ikb7, ikb8, ikb9)
    await bot.send_message(message.from_user.id, "вот ваши способы зароботка", reply_markup=earn_kb)


# 1
@dp.message_handler(commands=["Подписка"])
async def inst(message: types.Message, call: CallbackQuery):
    check_kb = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text="/перейти к аккаунту", url="https://www.instagram.com/nikky.kuznetsov")
    ikb2 = InlineKeyboardButton(text="/проверить подписку", callback_data="www")
    ikb3 = InlineKeyboardButton(text="/назад", callback_data="hello")
    check_kb.add(ikb1, ikb2, ikb3)
    check(call)
    await bot.send_message(message.from_user.id, "hello", reply_markup=check_kb)


# 2
@dp.message_handler(commands=["Подписка"])
async def inst(message: types.Message, call: CallbackQuery):
    check_kb = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text="/перейти к аккаунту", url="https://www.instagram.com/nikky.kuznetsov")
    ikb2 = InlineKeyboardButton(text="/проверить подписку", callback_data="www")
    ikb3 = InlineKeyboardButton(text="/назад", callback_data="hello")
    check_kb.add(ikb1, ikb2, ikb3)
    check(call)
    await bot.send_message(message.from_user.id, "hello", reply_markup=check_kb)


# 3
@dp.message_handler(commands=["Подписка"])
async def inst(message: types.Message, call: CallbackQuery):
    check_kb = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text="/перейти к аккаунту", url="https://www.instagram.com/nikky.kuznetsov")
    ikb2 = InlineKeyboardButton(text="/проверить подписку", callback_data="www")
    ikb3 = InlineKeyboardButton(text="/назад", callback_data="hello")
    check_kb.add(ikb1, ikb2, ikb3)
    check(call)
    await bot.send_message(message.from_user.id, "hello", reply_markup=check_kb)


# 1
@dp.message_handler(commands=["Подписка на канал"])
async def subs_channel(message: types.Message, call: CallbackQuery):
    check_kb = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text="/перейти к аккаунту", url="https://www.instagram.com/nikky.kuznetsov")
    ikb2 = InlineKeyboardButton(text="/проверить подписку", callback_data="www")
    ikb3 = InlineKeyboardButton(text="/назад", callback_data="hello")
    check_kb.add(ikb1, ikb2, ikb3)
    check_sub(call)
    await bot.send_message(message.from_user.id, "hello", reply_markup=check_kb)


# 2
@dp.message_handler(commands=["Подписка на канал"])
async def subsc_channel(message: types.Message, call: CallbackQuery):
    check_kb = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text="/перейти к аккаунту", url="https://www.instagram.com/nikky.kuznetsov")
    ikb2 = InlineKeyboardButton(text="/проверить подписку", callback_data="www")
    ikb3 = InlineKeyboardButton(text="/назад", callback_data="hello")
    check_kb.add(ikb1, ikb2, ikb3)
    check_sub(call)
    await bot.send_message(message.from_user.id, "hello", reply_markup=check_kb)


# 3
@dp.message_handler(commands=["Подписка на канал"])
async def subscr_channel(message: types.Message, call: CallbackQuery):
    check_kb = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text="/перейти к аккаунту", url="https://www.instagram.com/nikky.kuznetsov")
    ikb2 = InlineKeyboardButton(text="/проверить подписку", callback_data="www")
    ikb3 = InlineKeyboardButton(text="/назад", callback_data="hello")
    check_kb.add(ikb1, ikb2, ikb3)
    check_sub(call)
    await bot.send_message(message.from_user.id, "hello", reply_markup=check_kb)


# 4
@dp.message_handler(commands=["Подписка на канал"])
async def subscri_channel(message: types.Message, call: CallbackQuery):
    check_kb = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text="/перейти к аккаунту", url="https://www.instagram.com/nikky.kuznetsov")
    ikb2 = InlineKeyboardButton(text="/проверить подписку", callback_data="www")
    ikb3 = InlineKeyboardButton(text="/назад", callback_data="hello")
    check_kb.add(ikb1, ikb2, ikb3)
    check_sub(call)
    await bot.send_message(message.from_user.id, "hello", reply_markup=check_kb)


# 5
@dp.message_handler(commands=["Подписка на канал"])
async def subscrib_channel(message: types.Message, call: CallbackQuery):
    check_kb = InlineKeyboardMarkup(row_width=1)
    ikb1 = InlineKeyboardButton(text="/перейти к аккаунту", url="https://www.instagram.com/nikky.kuznetsov")
    ikb2 = InlineKeyboardButton(text="/проверить подписку", callback_data="www")
    ikb3 = InlineKeyboardButton(text="/назад", callback_data="hello")
    check_kb.add(ikb1, ikb2, ikb3)
    check_sub(call)
    await bot.send_message(message.from_user.id, "hello", reply_markup=check_kb)


@dp.message_handler(commands=["Пригласить"])
async def invite_friend(message: types.Message, call: CallbackQuery):
    url = "https://t.me/eazzzzzzzzzzzyyyyyymoneybot_bot"
    await bot.send_message(message.from_user.id, f'ссылка для приглашения: {url}')
    invite(call)


@dp.message_handler(commands=["balance"])
async def balance(message: types.Message, call: CallbackQuery):
    balance_kb = InlineKeyboardMarkup(row_width=1)
    balance_btn1 = InlineKeyboardButton(text="вывести")
    balance_kb.add(balance_btn1)

    if amount_balance < 30:
        await call.message.answer("вывод доступен при 30грн")

    else:
        await bot.send_message(message.chat.id, "щас покажем вам как вывести деньги")
    await bot.send_message(message.chat.id, f'💰 Ваш текущий баланс: {amount_balance} UAH', reply_markup=balance_kb)


def check(call: types.CallbackQuery):
    status = ["creator, administrator", "member"]
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001691522099", user_id=call.message.chat.id).status:
            check2(call)
            ++amount_balance
            print(amount_balance)

        else:
            bot.send_message(call.message.chat.id, "подпишитесь")


def check2(call, message):
    status = ["creator, administrator", "member"]
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001691522099", user_id=call.message.chat.id).status:
            bot.send_message(call.message.chat.id, "спасибо за подписку")
            bot.send_message(message.chat.id, reply_markup="")

        else:
            bot.send_message(call.message.chat.id, "подпишитесь")


def check_sub(call: types.CallbackQuery):
    status = ["creator, administrator", "member"]
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001691522099", user_id=call.message.chat.id).status:
            check_sub2(call)
            ++amount_balance

        else:
            bot.send_message(call.message.chat.id, "подпишитесь")


def check_sub2(call, message):
    status = ["creator, administrator", "member"]
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001691522099", user_id=call.message.chat.id).status:
            bot.send_message(call.message.chat.id, "спасибо за подписку")
            bot.send_message(message.chat.id, reply_markup="")
            break

        else:
            bot.send_message(call.message.chat.id, "подпишитесь")


def invite(call: types.CallbackQuery):
    status = ["creator, administrator", "member"]
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001691522099", user_id=call.message.chat.id).status:
            invite2(call)
            amount_balance = amount_balance +8

        else:
            bot.send_message(call.message.chat.id, "подпишитесь")


def invite2(call, message):
    status = ["creator, administrator", "member"]
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001691522099", user_id=call.message.chat.id).status:
            bot.send_message(call.message.chat.id, "спасибо за подписку")
            bot.send_message(message.chat.id, reply_markup="")
            break

        else:
            bot.send_message(call.message.chat.id, "подпишитесь")


executor.start_polling(dp, skip_updates=True)
