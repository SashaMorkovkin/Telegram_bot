import telebot
from telebot import types

bot = telebot.TeleBot("7728246242:AAFALiQAFSLjYiA7CP75kBubgTKzoxkahCQ")

name = ''
surname = ''
age = 0


@bot.message_handler(commands=['help'])
def help_handler(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, f'Себе помоги, {message.from_user.username}')


@bot.message_handler(commands=['reg'])
def start(message):
    bot.send_message(message.from_user.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_name)


@bot.message_handler(commabds=['problems'])
def get_problem(message):
    btns = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Нажмешь я нахуй тебе писюн отгрызу', callback_data='problem')
    btns.row(btn1)
    bot.reply_to(message, "Иди нахуй дон", reply_markup=btns)


@bot.callback_query_handler(func=lambda callback: True)
def callback_problems(callback):
    if callback.data == 'problem':
        bot.send_message(callback.from_user.id, "Пизда тебе, лысый")
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.from_user.id,
                         f"Пробил тебя по базе короче.\nИнформация следующая: \nИмя: {callback.from_user.name}\n"
                         f"Фамилия: {callback.from_user.surname}\n"
                         f"Номер телефона: {callback.from_user.phone}")


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    age = 0


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global age
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
        age = call.message
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Зубы лишние? : )')


bot.polling(none_stop=True, interval=0)
