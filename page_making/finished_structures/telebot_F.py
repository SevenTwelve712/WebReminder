from help.support.abspaths import static_pages
from pathlib import Path
from page_making.classes.instruction import Instruction
from page_making.classes.chapter_list import define_from_html
from help.support.abspaths import jinja_templs

code1 = """from telebot import *

bot = TeleBot('Token')
bot.infinity_polling()"""

code2 = """bot.send_message(message.chat.id, 'text')
# message.chat.id всего лишь пример переменной, так то нужен конкретный chatid"""

code3 = """bot.reply_to(message, text='text')
# message всего лишь пример переменной, так то нужно конкретное сообщение
# (внимание, не chatid, а именно сообщение)"""

code4 = """bot.send_photo(message.chat.id, open("C:\\Users\\seven\\Pictures\\Идеи для обоев\\6.jpg", 'rb'))
# bot.send_photo(chatid, open('Путь к файлу', 'rb'))
# Не сжатое фото"""

code5 = """bot.send_video(message.chat.id, open("C:\\Users\\seven\\Pictures\\1.mp4", 'rb'))
# bot.send_video(chatid, open('Путь к файлу', 'rb'))
# Не сжатое видео"""

code6 = """bot.send_audio(message.chat.id, open("C:\\Users\\seven\\Pictures\\Временка\\1.mp3", 'rb'))
# bot.send_audio(chatid, open('Путь к файлу', 'rb'))"""

code7 = """bot.send_document(message.chat.id, open("C:\\Users\\seven\\Pictures\\Временка\\1.ttf", 'rb'))
# bot.send_audio(chatid, open('Путь к файлу', 'rb'))
# если таким образом отправить изображение оно будет сжатым, но если отправить видео,
# оно будет не сжатым"""

code8 = """@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Пошел нахуй")
# Данный код отправит тому, кто запустил бота (автоматически отправляется команда /start)
# сообщение "Пошел нахуй"""

code9 = """@bot.message_handler(content_types=["text"])
def text_replyer(message):
    if message.text == 'Иди нахуй':
        bot.send_message(message.chat.id, "Сам нахуй иди шалава ебаная")
# Данный код отправит тому еблану, кто написал "Иди нахуй"
# сообщение "Сам нахуй иди шалава ебаная"""

code10 = """@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b1 = types.KeyboardButton(text="Suck dick")
    b2 = types.KeyboardButton(text="Fuck ass")
    b3 = types.KeyboardButton(text="Suction")
    b4 = types.KeyboardButton(text="Billy")
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Fuck you', reply_markup=markup)
# Данный код по команде \start отправит сообщение Fuck you пользователю, + у юзера появится поле
# с кнопками Suck dick, Fuck ass, Suction, Billy"""

code11 = """@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    b1 = types.InlineKeyboardButton(text="Suck dick", callback_data="gachi1")
    b2 = types.InlineKeyboardButton(text="Fuck ass", callback_data="gachi2")
    b3 = types.InlineKeyboardButton(text="Suction", callback_data="gachi3")
    b4 = types.InlineKeyboardButton(text="Billy", callback_data="gachi4")
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Fuck you', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "gachi1":
            bot.send_message(call.message.chat.id, "Without further interraption")
        elif call.data == "gachi2":
            bot.send_message(call.message.chat.id, "AAAAAAAAA")
        if call.data == "gachi3":
            bot.send_message(call.message.chat.id, "6 hot loads")
        if call.data == "gachi4":
            bot.send_message(call.message.chat.id, "Herrington")


# Данный код по команде \start отправит сообщение Fuck you пользователю, под которым будет 4 кнопки,
# на которых будет написано Suck dick, Fuck ass, Suction, Billy.
# При нажатии на Suck dick юзеру отправится сообщение Without further interraption
# При нажатии на Fuck ass юзеру отправится сообщение AAAAAAAAA
# При нажатии на Suction юзеру отправится сообщение 6 hot loads
# При нажатии на Billy юзеру отправится сообщение Herrington"""

chapter_list = define_from_html(jinja_templs + '/telebot.html')

kwargs = {
    'code1': code1,
    'code2': code2,
    'code3': code3,
    'code4': code4,
    'code5': code5,
    'code6': code6,
    'code7': code7,
    'code8': code8,
    'code9': code9,
    'code10': code10,
    'code11': code11,
}

instruction = Instruction(
    'telebot',
    'telebot.html',
    kwargs,
    chapter_list
)
instruction.make_static(Path(static_pages, 'telebot.html'))
