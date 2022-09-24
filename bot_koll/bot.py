from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from datetime import datetime
from config import TOKEN
from parsing_koll import days_dict

class Bot():
    def start():
        test()

def test():
    print('Bot start no проверки')
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    dict_test = {
        'понедельник' : 'пн',
        'вторник': 'вт',
        'среда': 'ср',
        'четверг': 'чт',
        'пятница': 'пт',
        'суббота': 'сб',
        'воскресенье' : 'вс',

        'пн': 'пн',
        'вт': 'вт',
        'ср': 'ср',
        'чт': 'чт',
        'пт': 'пт',
        'сб': 'сб',
        'вс': 'вс',

        1 : 'пн',
        2 : 'вт',
        3 : "ср",
        4 : "чт",
        5 : "пт",
        6 : "сб",
        7 : "вс",
    }

    week_list = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'понедельник', "вторник", "среда", "четверг", "пятница", "суббота"]

    #command 'start'
    @dp.message_handler(commands=['start'])
    async def welcome_user(msg: types.Message):


        #button "Получить расписание"
        kb = [
            [types.KeyboardButton(text="Сегодня"), types.KeyboardButton(text="Завтра")],
                [
                    types.KeyboardButton(text='Пн'),
                    types.KeyboardButton(text='Вт'),
                    types.KeyboardButton(text='Ср'),
                ],
                [
                    types.KeyboardButton(text='Чт'),
                    types.KeyboardButton(text='Пт'),
                    types.KeyboardButton(text='Сб'),
                ]
            ]

        markup = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

        await msg.answer(f"""
        Привет <b>{msg.from_user.last_name}</b>!
    Это тестовый бот который показывает расписание пар в колледже ПГУТИ КС.\nДля работы нужно указать дни недели 
        """, parse_mode="HTML", reply_markup=markup)


    #all message
    @dp.message_handler()
    async def lalala(msg: types.Message):

        if msg.text.lower() == "пашел нахуй":
            await msg.answer('Сам пашёл нахуй')

        elif msg.text.lower() == 'сегодня':
            today = dict_test[datetime.isoweekday(datetime.now())]
            if days_dict[today] == 'Выходной':
                await msg.answer('Сегодня выходной, иди спи')
            else:
                for items in days_dict[today]:
                    await msg.answer(f'Пара: {items[0]}\nВремя: {items[1]}\nКабинет:{items[4]}\nПрепод: {items[3]}\nПредмет: <b>{items[2]}</b>', parse_mode='HTML')


        elif msg.text.lower() == 'завтра':
            today = dict_test[datetime.isoweekday(datetime.now())+1]
            if days_dict[today] == 'Выходной':
                await msg.answer('Завтра выходной, можно отдыхать')
            else:
                for items in days_dict[today]:
                    await msg.answer(f'Пара: {items[0]}\nВремя: {items[1]}\nКабинет:{items[4]}\nПрепод: {items[3]}\nПредмет: <b>{items[2]}</b>', parse_mode='HTML')


        elif msg.text.lower() in week_list:
            for items in days_dict[dict_test[msg.text.lower()]]:
                await msg.answer(f'Пара: {items[0]}\nВремя: {items[1]}\nКабинет:{items[4]}\nПрепод: {items[3]}\nПредмет: <b>{items[2]}</b>', parse_mode='HTML')    


        else:
            await msg.answer('Я не знаю как на такое ответить😕')



    # if __name__ == '__main__':
    print('Bot starting')
    executor.start_polling(dp)






# Код который сохраню что бы на будущее вспонил как работает он для учебы короче

# Кнопки в сообщении(Inline)

    # inline_kb = types.InlineKeyboardMarkup()
    # kb_inline_btn1 = types.InlineKeyboardButton('Пн', callback_data='button_пн')
    # kb_inline_btn2 = types.InlineKeyboardButton('Вт', callback_data='button_вт')
    # kb_inline_btn3 = types.InlineKeyboardButton('Ср', callback_data='button_ср')
    # kb_inline_btn4 = types.InlineKeyboardButton('Чт', callback_data='button_чт')
    # kb_inline_btn5 = types.InlineKeyboardButton('Пт', callback_data='button_пт')
    # kb_inline_btn6 = types.InlineKeyboardButton('Сб', callback_data='button_сб')
    # inline_kb.add(kb_inline_btn1, kb_inline_btn2, kb_inline_btn3, kb_inline_btn4, kb_inline_btn5, kb_inline_btn6)

# Обрабатываем inline кнопки

# @dp.callback_query_handler(Text(startswith='button'))
# async def pn_week(collback: types.CallbackQuery):
#     res = collback.data.split('_')[1]
#     await collback.message.answer(f'    {week_time[days_dict[res][0][-1]]}    ')
#     for items in days_dict[res]:
#         await collback.message.answer(f'Пара: {items[0]}\nВремя: {items[1]}\nКабинет:{items[4]}\nПрепод: {items[3]}\nПредмет: <b>{items[2]}</b>', parse_mode='HTML')
#     await collback.answer()
