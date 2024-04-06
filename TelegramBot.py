import telebot
from telebot import types


bot = telebot.TeleBot('7104415538:AAFJFVuLi5eALVknElHS_KEnp6nq1C9VMWU')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('start', callback_data='start')
    item2 = types.InlineKeyboardButton(text='news', url='https://rb.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=msk_poisk_general_keys&utm_term=---autotargeting&utm_content=premium_1&yclid=3893703474623283199')
    keyboard.add(item, item2)
    bot.send_message(message.chat.id, '<b>Приветствую тебя кожаный👋 </b>', reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['news'])
def get_news(message):
    keyboard = types.InlineKeyboardMarkup()
    url_bth = types.InlineKeyboardButton(text='news', url='https://rb.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=msk_poisk_general_keys&utm_term=---autotargeting&utm_content=premium_1&yclid=3893703474623283199')
    keyboard.add(url_bth)
    bot.send_message(message.chat.id, 'news', reply_markup=keyboard)

@bot.message_handler()
def get_user_text(mass):
    if mass.text == 'Привет':
        hi = f'И тебе привет, <b>{mass.from_user.first_name} <u>{mass.from_user.last_name}</u></b>'
        bot.send_message(mass.chat.id, hi, parse_mode='html')
    else:
        bot.send_message(mass.chat.id, 'Я тебя не понимаю', parse_mode='html')



bot.polling(none_stop=True)











#pip install pyTelegramBotAPI - вызов библиотеки
#pip install pytelegrambotapi --upgrade апгрейд библиотеки бота

        # mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>' #вызов фио
        # bot.send_message(message.chat.id, mess, parse_mode='html') #вызов фио



    #bot.send_message(message.chat.id, '<b>Приветствую тебя кожаный ублюдок</b>', parse_mode='html')

#@bot.message_handler(commands=['hello'])
#def hello(message):
   # mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
#@bot.message_handler()
#def get_user_text(mass):
    #if mass.text == 'Привет':
       # bot.send_message(mess.chat.id, '<b>И тебе привет</b>', parse_mode='html')
    #else:bot.send_message(mess.chat.id, '<b>Я тебя не понимаю</b>', parse_mode='html')